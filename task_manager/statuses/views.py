from django.contrib import messages
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

from task_manager.mixins import LoginMixin
from task_manager.tasks.models import Task

from .forms import StatusForm
from .models import Status


class IndexStatusesView(LoginMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        statuses = Status.objects.all().order_by("id")
        return render(
            request, "statuses/index.html", context={"statuses": statuses}
        )


class CreateStatusesView(LoginMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = "statuses/create.html"
    success_url = reverse_lazy("statuses:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _("Status successfully created"))
        return response


class UpdateStatusesView(LoginMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = "statuses/update.html"
    success_url = reverse_lazy("statuses:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _("Status successfully updated"))
        return response


class DeleteStatusesView(LoginMixin, DeleteView):
    model = Status
    template_name = "statuses/delete.html"
    success_url = reverse_lazy("statuses:index")

    def form_valid(self, form):
        if Task.objects.filter(status=self.object).exists():
            messages.error(
                self.request, _("Cannot delete status because it is in use")
            )
            return redirect("statuses:index")
        response = super().form_valid(form)
        messages.success(self.request, _("Status successfully deleted"))
        return response
