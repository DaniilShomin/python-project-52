from django.contrib import messages
from django.db.models import ProtectedError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from task_manager.mixins import CustomLoginMixin
from task_manager.tasks.models import Task
from task_manager.users.forms import UserForm
from task_manager.users.models import User


class IndexUserView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        users = User.objects.all().order_by("id")
        return render(
            request,
            "users/index.html",
            context={"users": users},
        )


class CreateUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = "users/create.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.save()

        messages.success(self.request, _("User registered successfully"))

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Registration")
        return context


class UpdateUserView(CustomLoginMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "users/update.html"
    success_url = reverse_lazy("users:index")

    def form_valid(self, form):
        """Обработка ВАЛИДНОЙ формы"""
        if "password1" in form.cleaned_data and form.cleaned_data["password1"]:
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
        else:
            form.save()

        messages.success(self.request, _("User successfully changed."))
        return super().form_valid(form)

    def form_invalid(self, form):
        """Обработка НЕВАЛИДНОЙ формы"""
        messages.error(self.request, _("Please correct the errors below."))
        return super().form_invalid(form)


class DeleteUserView(CustomLoginMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users:index")

    def get_context_data(self, **kwargs):
        """Добавление информации о связанных задачах в контекст"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()

        context["has_related_tasks"] = Task.objects.filter(
            executor=user
        ).exists()
        context["task_count"] = Task.objects.filter(executor=user).count()

        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Обработка удаления с проверкой связей"""
        user = self.get_object()

        if Task.objects.filter(executor=user).exists():
            messages.error(
                request, _("Cannot delete user because it is in use")
            )
            return redirect("users:index")

        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(request, _("User successfully deleted"))
            return response
        except ProtectedError:
            # Защита от каскадного удаления (если настроены on_delete=PROTECT)
            messages.error(
                request,
                _(
                    "Cannot delete user "
                    "because it is referenced by other records."
                ),
            )
            return redirect("users:index")
