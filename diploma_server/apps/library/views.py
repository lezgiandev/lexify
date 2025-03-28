from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, serializers, status, filters, response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.library.models import Book, Sentence, CompletedBook, Category
from apps.library.serializers import BookSerializer, SentenceSerializer, CompletedBookSerializer, CategorySerializer
from apps.user.models import User


class BookCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class LibraryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'author']

    def get_queryset(self):
        if isinstance(self.request.user, User) and hasattr(self.request.user, 'language'):
            return Book.objects.filter(
                language=self.request.user.language
            ).order_by("title")
        return Book.objects.none()

    @action(detail=True, methods=['get'], url_path='sentences')
    def list_sentences(self, request, pk=None):
        book = self.get_object()
        sentences = Sentence.objects.filter(book=book)
        serializer = SentenceSerializer(sentences, many=True)
        return Response(serializer.data)


class CompletedBookViewSet(viewsets.ModelViewSet):
    serializer_class = CompletedBookSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        if isinstance(self.request.user, User):
            return CompletedBook.objects.filter(
                user=self.request.user,
                book__language=self.request.user.language
            ).order_by('book__title')
        return CompletedBook.objects.none()

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            book_id = serializer.validated_data['book'].id
            if CompletedBook.objects.filter(user=self.request.user, book_id=book_id).exists():
                raise serializers.ValidationError("Эта книга уже в прочитанном!")
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError("Пользователь не авторизован!")

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