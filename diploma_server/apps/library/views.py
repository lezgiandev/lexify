from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, serializers, status, filters, response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.library.models import Book, Sentence, CompletedBook, Category
from apps.library.serializers import BookSerializer, SentenceSerializer, CompletedBookSerializer, CategorySerializer
from apps.user.models import User


class BookCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для работы с категориями книг
    """
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(
        operation_description="Получить список всех категорий книг",
        responses={200: CategorySerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class LibraryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для работы с библиотекой книг
    """
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'author']

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
                description="Поиск по названию или автору",
                type=openapi.TYPE_STRING
            )
        ]
    )
    def get_queryset(self):
        if isinstance(self.request.user, User) and hasattr(self.request.user, 'language'):
            return Book.objects.filter(
                language=self.request.user.language
            ).order_by("title")
        return Book.objects.none()

    @swagger_auto_schema(
        methods=['get'],
        operation_description="Получить список предложений для книги",
        responses={
            200: SentenceSerializer(many=True),
            404: "Книга не найдена"
        }
    )
    @action(detail=True, methods=['get'], url_path='sentences')
    def list_sentences(self, request, pk=None):
        book = self.get_object()
        sentences = Sentence.objects.filter(book=book)
        serializer = SentenceSerializer(sentences, many=True)
        return Response(serializer.data)


class CompletedBookViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с прочитанными книгами
    """
    serializer_class = CompletedBookSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    @swagger_auto_schema(
        operation_description="Получить список прочитанных книг",
        responses={200: CompletedBookSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Добавить книгу в прочитанные",
        responses={
            201: CompletedBookSerializer,
            400: "Книга уже в прочитанных",
            401: "Не авторизован"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            book_id = serializer.validated_data['book'].id
            if CompletedBook.objects.filter(user=self.request.user, book_id=book_id).exists():
                raise serializers.ValidationError("Эта книга уже в прочитанном!")
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError("Пользователь не авторизован!")

    @swagger_auto_schema(
        methods=['delete'],
        operation_description="Удалить книгу из прочитанных по ID",
        manual_parameters=[
            openapi.Parameter(
                'book_id',
                openapi.IN_QUERY,
                description="ID книги для удаления",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={
            204: "Успешное удаление",
            400: "Не указан book_id",
            404: "Книга не найдена в прочитанных"
        }
    )
    @action(detail=False, methods=['delete'], url_path='delete')
    def remove_by_book(self, request):
        book_id = request.query_params.get('book_id')
        if not book_id:
            return Response({"detail": "Необходимо указать book_id."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            completed_book = CompletedBook.objects.get(
                user=request.user,
                book_id=book_id
            )
            completed_book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CompletedBook.DoesNotExist:
            return Response({"detail": "Книга не найдена в прочитанном."}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        methods=['delete'],
        operation_description="Удалить все прочитанные книги",
        responses={
            204: "Все книги удалены",
            404: "Книги не найдены"
        }
    )
    @action(detail=False, methods=['delete'], url_path='delete-all')
    def delete_all_completed(self, request):
        try:
            CompletedBook.objects.filter(user=request.user).delete()
            return Response(
                {"detail": "Все прочитанные книги удалены"},
                status=status.HTTP_204_NO_CONTENT
            )
        except CompletedBook.DoesNotExist:
            return Response({"detail": "Книги не найдены в прочитанном."}, status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        if isinstance(self.request.user, User):
            return CompletedBook.objects.filter(
                user=self.request.user,
                book__language=self.request.user.language
            ).order_by('book__title')
        return CompletedBook.objects.none()