from django.utils import timezone
from hospital.authentication.models import AuthToken
from rest_framework.authentication import TokenAuthentication as DRFTokenAuthenticationClass


class CustomTokenAuthentication(DRFTokenAuthenticationClass):
    model = AuthToken

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        user.last_activity = timezone.now()
        user.save(update_fields=['last_activity'])
        return user, token
