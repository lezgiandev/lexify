from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, response, filters, serializers, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.sourcelink.models import Category, Source, MarkedSource
from apps.sourcelink.serializers import CategorySerializer, SourceSerializer, MarkedSourceSerializer
from apps.user.models import User


class SourceCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class SourceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['text']

    def get_queryset(self):
        if isinstance(self.request.user, User) and hasattr(self.request.user, 'language'):
            return Source.objects.filter(
                language=self.request.user.language
            ).order_by("text")
        return Source.objects.none()


class MarkedSourceViewSet(viewsets.ModelViewSet):
    serializer_class = MarkedSourceSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        if isinstance(self.request.user, User):
            return MarkedSource.objects.filter(
                user=self.request.user,
                source__language=self.request.user.language
            ).order_by('source__text')
        return MarkedSource.objects.none()

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            source_id = serializer.validated_data['source'].id
            if MarkedSource.objects.filter(user=self.request.user, source_id=source_id).exists():
                raise serializers.ValidationError("Эта ссылка уже отмечена!")
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError("Пользователь не авторизован!")

    @action(detail=False, methods=['delete'], url_path='delete')
    def remove_by_source(self, request):
        source_id = request.query_params.get('source_id')
        if not source_id:
            return Response({"detail": "Необходимо указать source_id."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            marked_book = MarkedSource.objects.get(
                user=request.user,
                source_id=source_id
            )
            marked_book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MarkedSource.DoesNotExist:
            return Response({"detail": "Ссылка на ресурс не найдена в отмеченном."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['delete'], url_path='delete-all')
    def delete_all_marks(self, request):
        try:
            MarkedSource.objects.filter(user=request.user).delete()
            return Response(
                {"detail": "Все отмеченные источники удалены"},
                status=status.HTTP_204_NO_CONTENT
            )
        except MarkedSource.DoesNotExist:
            return Response({"detail": "Источники не найдены в отмеченном."}, status=status.HTTP_404_NOT_FOUND)