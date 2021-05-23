from rest_framework.routers import DefaultRouter

from hospital.user.api.v1.views.user import UserViewSet

ROUTER = DefaultRouter()

ROUTER.register('', UserViewSet, basename='user')

urlpatterns = ROUTER.urls
