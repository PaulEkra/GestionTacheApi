from rest_framework import viewsets
from ..models.task_history_model import TaskHistoryModel
from ..serializers.task_history_serializer import TaskHistorySerializer

from rest_framework import filters
from ..pagination import StandardResultsSetPagination


# Create your views here.
class HistoriesViewset(viewsets.ModelViewSet):
    queryset = TaskHistoryModel.objects.all()
    serializer_class = TaskHistorySerializer
    http_method_names = ['get']
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ("updated_by", "task")
