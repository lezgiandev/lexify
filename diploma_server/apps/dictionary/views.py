from rest_framework import viewsets, filters, serializers, status, response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Translation, FavoriteWord, Category, PartOfSpeech
from .serializers import TranslationSerializer, FavoriteWordSerializer, CategorySerializer, PartOfSpeechSerializer
from apps.user.models import User


class DictionaryCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class PartOfSpeechViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PartOfSpeech.objects.all()
    serializer_class = PartOfSpeechSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class DictionaryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TranslationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['word__category', 'word__part_of_speech']
    search_fields = ['text', 'word__text']

    def get_queryset(self):
        if isinstance(self.request.user, User) and hasattr(self.request.user, 'language'):
            return Translation.objects.filter(
                language=self.request.user.language
            ).order_by("word__text")
        return Translation.objects.none()


class FavoriteWordViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteWordSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        if isinstance(self.request.user, User):
            return FavoriteWord.objects.filter(
                user=self.request.user,
                translation__language=self.request.user.language
            ).order_by('translation__id')
        return FavoriteWord.objects.none()

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            translation_id = serializer.validated_data['translation'].id
            if FavoriteWord.objects.filter(user=self.request.user, translation_id=translation_id).exists():
                raise serializers.ValidationError("Это слово уже в избранном!")
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError("Пользователь не авторизован!")

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

    @action(detail=False, methods=['get'], url_path='check-favorite')
    def check_favorite(self, request):
        translation_id = request.query_params.get('translation_id')
        if not translation_id:
            return Response({"detail": "Необходимо указать translation_id."}, status=400)

        is_favorite = FavoriteWord.objects.filter(
            user=request.user,
            translation_id=translation_id
        ).exists()

        return Response({"is_favorite": is_favorite})

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