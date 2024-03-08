from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from ..serializers.api.users import RegistrationSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema


User = get_user_model()


@extend_schema_view(
    post=extend_schema(summary='Регистрация Пользователя', tags=['Авторизация и Аутентификация'])
)
class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]