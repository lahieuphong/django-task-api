from django.contrib import admin
from .models import Project, Tag, Task, TaskDetail


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name", "description")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "color")
    search_fields = ("name",)


class TaskDetailInline(admin.StackedInline):
    model = TaskDetail
    extra = 1
    max_num = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "project", "is_done", "created_at")
    search_fields = ("title", "description")
    list_filter = ("project", "is_done", "tags")
    inlines = [TaskDetailInline]
