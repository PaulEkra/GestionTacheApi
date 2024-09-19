from rest_framework import serializers
from project.models.summons_model import SummonsModel

from project.models.task_model import TaskModel


class SummonsSerializer(serializers.ModelSerializer):
    task = serializers.SlugRelatedField(
        read_only = True,
        slug_field='title'
    )
    task_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TaskModel.objects.filter(progress="todo"),
                                                    source='task')
    class Meta:
        model = SummonsModel
        fields = '__all__'
        read_only_fields = ['id', 'status', 'created_at', 'update_at']
