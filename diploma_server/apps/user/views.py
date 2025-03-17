from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, LanguageUpdateSerializer, UserLanguageSerializer, ChangePasswordSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LanguageUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def put(request):
        serializer = LanguageUpdateSerializer(data=request.data)
        if serializer.is_valid():
            request.user.language = serializer.validated_data['language_id']
            request.user.save()
            return Response({'status': 'User language was updated!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LanguageRetrieveView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        serializer = UserLanguageSerializer(request.user)
        return Response(serializer.data)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"status": "Пароль успешно изменен"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        serializer = UserLanguageSerializer(request.user)
        return Response(serializer.data)