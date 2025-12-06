from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)

from task_manager.mixins import LoginMixin, TaskMixin
from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task


class IndexTaskView(LoginMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        tasks = Task.objects.all()
        filterset = TaskFilter(request.GET, queryset=tasks, request=request)
        return render(
            request,
            "tasks/index.html",
            context={
                "form": filterset.form,
                "tasks": filterset.qs,
            },
        )


class CreateTaskView(LoginMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create.html"
    success_url = reverse_lazy("tasks:index")

    def form_valid(self, form):
        task = form.save(commit=False)
        task.author = self.request.user
        task.save()
        response = super().form_valid(form)
        messages.success(self.request, _("Task successfully created"))
        return response


class UpdateTaskView(LoginMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/update.html"
    success_url = reverse_lazy("tasks:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _("Task successfully updated"))
        return response


class DeleteTaskView(TaskMixin, DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _("Task successfully deleted"))
        return response


class ShowTaskView(LoginMixin, View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        task = get_object_or_404(Task, pk=pk)
        return render(request, "tasks/show.html", context={"task": task})
