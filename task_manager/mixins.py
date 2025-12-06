from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class CustomLoginMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = "/login/"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _("You are not logged in! Please sign in."))
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        """Проверяем права доступа - UserPassesTestMixin"""
        user = self.get_object()  # UpdateView сам получает объект
        return self.request.user.is_superuser or self.request.user.id == user.id

    def handle_no_permission(self):
        """Если нет прав - показываем ошибку и редирект"""
        messages.error(
            self.request,
            _("You do not have permission to change another user."),
        )
        return redirect(self.success_url)
