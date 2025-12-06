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

    def post(self, request: HttpRequest) -> HttpResponse:
        form = self.get_form()
        if form.is_valid():
            messages.success(request, _("You are login"))
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("index")


class CustomLogoutView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        messages.info(request, _("You are logout"))
        return redirect("index")
