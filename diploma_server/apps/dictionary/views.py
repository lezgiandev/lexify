from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, filters, serializers, status, response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Translation, FavoriteWord, Category, PartOfSpeech, Word
from .serializers import TranslationSerializer, FavoriteWordSerializer, CategorySerializer, PartOfSpeechSerializer, \
    WordSerializer
from apps.user.models import User


class DictionaryCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для работы с категориями словаря
    """
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(
        operation_description="Получить список всех категорий словаря",
        responses={200: CategorySerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class PartOfSpeechViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для работы с частями речи
    """
    permission_classes = [IsAuthenticated]
    queryset = PartOfSpeech.objects.all()
    serializer_class = PartOfSpeechSerializer

    @swagger_auto_schema(
        operation_description="Получить список всех частей речи",
        responses={200: PartOfSpeechSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class DictionaryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для работы со словарем
    """
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'part_of_speech']
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
                'part_of_speech',
                openapi.IN_QUERY,
                description="Фильтр по ID части речи",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'search',
                openapi.IN_QUERY,
                description="Поиск по тексту слова",
                type=openapi.TYPE_STRING
            )
        ]
    )
    def get_queryset(self):
        if isinstance(self.request.user, User):
            return Word.objects.order_by("text")
        return Word.objects.none()

    @swagger_auto_schema(
        methods=['get'],
        operation_description="Получить переводы для конкретного слова",
        responses={
            200: TranslationSerializer(many=True),
            404: "Слово не найдено",
            500: "Внутренняя ошибка сервера"
        }
    )
    @action(detail=True, methods=['get'], url_path='translations')
    def list_translations(self, request, pk=None):
        try:
            word = self.get_object()
            translations = Translation.objects.filter(
                word=word,
                language=request.user.language
            )
            serializer = TranslationSerializer(translations, many=True)
            return Response(serializer.data)
        except NotFound:
            return Response({"detail": "Слово не найдено."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(
                {"detail": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class FavoriteWordViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с избранными словами
    """
    serializer_class = FavoriteWordSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    @swagger_auto_schema(
        operation_description="Получить список избранных слов пользователя",
        responses={200: FavoriteWordSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Добавить слово в избранное",
        responses={
            201: FavoriteWordSerializer,
            400: "Слово уже в избранном",
            401: "Не авторизован"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            translation_id = serializer.validated_data['translation'].id
            if FavoriteWord.objects.filter(user=self.request.user, translation_id=translation_id).exists():
                raise serializers.ValidationError("Это слово уже в избранном!")
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError("Пользователь не авторизован!")

    @swagger_auto_schema(
        methods=['delete'],
        operation_description="Удалить слово из избранного по ID перевода",
        manual_parameters=[
            openapi.Parameter(
                'translation_id',
                openapi.IN_QUERY,
                description="ID перевода для удаления",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={
            204: "Успешное удаление",
            400: "Не указан translation_id",
            404: "Слово не найдено в избранном"
        }
    )
    @action(detail=False, methods=['delete'], url_path='delete')
    def remove_by_translation(self, request):
        translation_id = request.query_params.get('translation_id')
        if not translation_id:
            return Response({"detail": "Необходимо указать translation_id."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            favorite_word = FavoriteWord.objects.get(
                user=request.user,
                translation_id=translation_id
            )
            favorite_word.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FavoriteWord.DoesNotExist:
            return Response({"detail": "Слово не найдено в избранном."}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        methods=['delete'],
        operation_description="Удалить все избранные слова пользователя",
        responses={
            204: "Все слова удалены",
            404: "Слова не найдены"
        }
    )
    @action(detail=False, methods=['delete'], url_path='delete-all')
    def delete_all_favorites(self, request):
        try:
            FavoriteWord.objects.filter(user=request.user).delete()
            return Response(
                {"detail": "Все избранные слова удалены"},
                status=status.HTTP_204_NO_CONTENT
            )
        except FavoriteWord.DoesNotExist:
            return Response({"detail": "Слова не найдены в избранном."}, status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        if isinstance(self.request.user, User):
            return FavoriteWord.objects.filter(
                user=self.request.user,
                translation__language=self.request.user.language
            ).order_by('translation__id')
        return FavoriteWord.objects.none()