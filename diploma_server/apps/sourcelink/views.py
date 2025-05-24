from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, response, filters, serializers, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.sourcelink.models import Category, Source, MarkedSource
from apps.sourcelink.serializers import CategorySerializer, SourceSerializer, MarkedSourceSerializer
from apps.user.models import User


class SourceCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для работы с категориями источников
    """
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(
        operation_description="Получить список всех категорий источников",
        responses={200: CategorySerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class SourceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для работы с источниками
    """
    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['text']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'category',
                openapi.IN_QUERY,
                description="Фильтр по ID категории",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'search',
                openapi.IN_QUERY,
                description="Поиск по тексту источника",
                type=openapi.TYPE_STRING
            )
        ]
    )
    def get_queryset(self):
        if isinstance(self.request.user, User) and hasattr(self.request.user, 'language'):
            return Source.objects.filter(
                language=self.request.user.language
            ).order_by("text")
        return Source.objects.none()


class MarkedSourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с отмеченными источниками
    """
    serializer_class = MarkedSourceSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    @swagger_auto_schema(
        operation_description="Получить список отмеченных источников",
        responses={200: MarkedSourceSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Добавить источник в отмеченные",
        responses={
            201: MarkedSourceSerializer,
            400: "Источник уже отмечен",
            401: "Не авторизован"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            source_id = serializer.validated_data['source'].id
            if MarkedSource.objects.filter(user=self.request.user, source_id=source_id).exists():
                raise serializers.ValidationError("Эта ссылка уже отмечена!")
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError("Пользователь не авторизован!")

    @swagger_auto_schema(
        methods=['delete'],
        operation_description="Удалить источник из отмеченных по ID",
        manual_parameters=[
            openapi.Parameter(
                'source_id',
                openapi.IN_QUERY,
                description="ID источника для удаления",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={
            204: "Успешное удаление",
            400: "Не указан source_id",
            404: "Источник не найден в отмеченных"
        }
    )
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

    @swagger_auto_schema(
        methods=['delete'],
        operation_description="Удалить все отмеченные источники",
        responses={
            204: "Все источники удалены",
            404: "Источники не найдены"
        }
    )
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

    def get_queryset(self):
        if isinstance(self.request.user, User):
            return MarkedSource.objects.filter(
                user=self.request.user,
                source__language=self.request.user.language
            ).order_by('source__text')
        return MarkedSource.objects.none()