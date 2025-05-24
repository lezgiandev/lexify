from drf_yasg.utils import swagger_auto_schema
from rest_framework import response, viewsets
from rest_framework.permissions import IsAuthenticated
from apps.alphabet.models import Letter
from apps.alphabet.serializers import LetterSerializer


class LetterListView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

    @swagger_auto_schema(
        operation_description="Получить список всех букв",
        responses={200: LetterSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)