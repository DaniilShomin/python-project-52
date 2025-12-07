from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "index.html", context={})


class CustomLoginView(LoginView):
    template_name = "login.html"

    def form_valid(self, form) -> HttpResponse:
        response = super().form_valid(form)
        messages.success(self.request, _("You are login"))
        return response

    def get_success_url(self):
        return reverse_lazy("index")


class CustomLogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        """GET запросы перенаправляем на главную"""
        return redirect("index")

    def post(self, request: HttpRequest) -> HttpResponse:
        """Выход через POST для безопасности"""
        if request.user.is_authenticated:
            logout(request)
            messages.info(request, _("You are logout"))
        else:
            messages.warning(request, _("You are not logged in"))

        return redirect("index")
