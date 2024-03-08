from django.urls import path, include
from .views import users

urlpatterns = [
    path('users/reg/', users.RegistrationView.as_view(), name='reg'),
]