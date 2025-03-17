from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from apps.alphabet.views import LetterListView
from apps.dictionary.views import DictionaryCategoryViewSet, PartOfSpeechViewSet, DictionaryViewSet, FavoriteWordViewSet
from apps.language.views import LanguageListView
from apps.library.views import LibraryViewSet, CompletedBookViewSet
from apps.sourcelink.views import SourceViewSet, MarkedSourceViewSet, SourceCategoryViewSet
from apps.texttospeech.views import GenerateAudioView
from apps.user.views import RegisterView, LanguageUpdateView, LanguageRetrieveView, ChangePasswordView

router = DefaultRouter()
router.register(r'dictionary-categories', DictionaryCategoryViewSet, basename='dictionary-categories')
router.register(r'parts-of-speech', PartOfSpeechViewSet, basename='parts-of-speech')
router.register(r'dictionary', DictionaryViewSet, basename='dictionary')
router.register(r'favorite-words', FavoriteWordViewSet, basename='favorite-words')
router.register(r'library', LibraryViewSet, basename='library')
router.register(r'completed-books', CompletedBookViewSet, basename='completed-books')
router.register(r'sources', SourceViewSet, basename='sources')
router.register(r'marked-sources', MarkedSourceViewSet, basename='marked-sources')
router.register(r'source-categories', SourceCategoryViewSet, basename='source-categories')
router.register(r'alphabet', LetterListView, basename="alphabet")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/languages/', LanguageListView.as_view(), name='languages'),
    path('api/user/change-language/', LanguageUpdateView.as_view(), name='change-language'),
    path('api/check-language/', LanguageRetrieveView.as_view(), name='check-language'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/generate-audio/', GenerateAudioView.as_view(), name='generate-audio'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)