from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ParseError
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')


    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise ParseError('Email already registered')
        return email

    def validate_password(self, value):
        validate_password(value)
        return value