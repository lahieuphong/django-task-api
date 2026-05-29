from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.db.models import Count
from rest_framework import viewsets
from .models import Project, Tag, Task
from .serializers import ProjectSerializer, TagSerializer, TaskSerializer


@ensure_csrf_cookie
def home(request):
    return render(request, "tasks/index.html")


class TaskViewSet(viewsets.ModelViewSet):
    queryset = (
        Task.objects.select_related("project", "detail")
        .prefetch_related("tags")
        .order_by("-created_at")
    )
    serializer_class = TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.annotate(task_count=Count("tasks")).order_by("-created_at")
    serializer_class = ProjectSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by("name")
    serializer_class = TagSerializer
