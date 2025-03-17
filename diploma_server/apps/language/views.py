from rest_framework import generics, response
from rest_framework.permissions import AllowAny
from apps.language.models import Language
from apps.language.serializers import LanguageSerializer


class LanguageListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)