from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TagViewSet, TaskViewSet


router = DefaultRouter()
router.register("projects", ProjectViewSet, basename="project")
router.register("tags", TagViewSet, basename="tag")
router.register("tasks", TaskViewSet, basename="task")

app_name = "tasks"

urlpatterns = [
    path("", include(router.urls)),
]
