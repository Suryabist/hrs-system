from django.urls import path

from hospital.authentication.api.v1.views.register import UserRegistrationView
from hospital.authentication.api.v1.views.token import ObtainAuthTokenView, DeleteAuthToken

urlpatterns = [
    path('sign-up/', UserRegistrationView.as_view(), name='user-register'),
    path('auth-token/', ObtainAuthTokenView.as_view(), name='auth-token'),
    path('delete-token/', DeleteAuthToken.as_view(), name='delete-auth-token'),
]
