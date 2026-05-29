from rest_framework import serializers
from .models import Project, Tag, Task, TaskDetail


class ProjectSerializer(serializers.ModelSerializer):
    task_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "created_at", "task_count"]
        read_only_fields = ["id", "created_at", "task_count"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "color"]
        read_only_fields = ["id"]


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDetail
        fields = ["id", "priority", "deadline", "note"]
        read_only_fields = ["id"]


class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        source="project",
        write_only=True,
        required=False,
        allow_null=True,
    )
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        source="tags",
        many=True,
        write_only=True,
        required=False,
    )
    detail = TaskDetailSerializer(required=False)

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "is_done",
            "created_at",
            "project",
            "project_id",
            "tags",
            "tag_ids",
            "detail",
        ]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        detail_data = validated_data.pop("detail", {})
        task = Task.objects.create(**validated_data)
        task.tags.set(tags)
        TaskDetail.objects.create(task=task, **detail_data)
        return task

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", None)
        detail_data = validated_data.pop("detail", None)

        task = super().update(instance, validated_data)

        if tags is not None:
            task.tags.set(tags)

        if detail_data is not None:
            TaskDetail.objects.update_or_create(
                task=task,
                defaults=detail_data,
            )

        return task
