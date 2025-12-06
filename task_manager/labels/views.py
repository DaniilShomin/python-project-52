from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.mixins import LoginMixin
from task_manager.tasks.models import Task


class IndexLabelsView(LoginMixin, View):
    def get(self, request):
        labels = Label.objects.all()
        return render(request, "labels/index.html", context={"labels": labels})


class CreateLabelsView(LoginMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = "labels/create.html"
    success_url = reverse_lazy("labels:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _("The label was successfully created."))
        return response


class UpdateLabelsView(LoginMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = "labels/update.html"
    success_url = reverse_lazy("labels:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _("Label successfully updated"))
        return response


class DeleteLabelsView(LoginMixin, DeleteView):
    model = Label
    template_name = "labels/delete.html"
    success_url = reverse_lazy("labels:index")

    def form_valid(self, form):
        if Task.objects.filter(labels=self.object).exists():
            messages.error(
                self.request, _("Cannot delete label because it is in use")
            )
            return redirect("labels:index")
        response = super().form_valid(form)
        messages.success(self.request, _("Label successfully deleted"))
        return response
