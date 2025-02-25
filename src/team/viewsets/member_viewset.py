from django.http import JsonResponse
from rest_framework import viewsets
from team.serializers.member_serializer import MemberSerializer,MemberTaskSerializer
from team.models.member_model import MemberModel
from rest_framework.decorators import action


class MemberViewSet(viewsets.ModelViewSet):
    queryset = MemberModel.objects.filter(status=True)
    serializer_class = MemberSerializer

    @action(detail=True, methods=['get'])
    def task(self, request, pk=None):
        member = self.get_object()
        serializer = MemberTaskSerializer(member)
        return JsonResponse(serializer.data, status=200)

