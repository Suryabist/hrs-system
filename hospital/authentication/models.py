from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.authtoken.models import Token as DRFAuthTokenModel
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from hospital.core.models import hospitals

USER = get_user_model()


class AuthToken(DRFAuthTokenModel):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='auth_tokens')
    device_id = models.CharField(
        verbose_name=_("Device ID"),
        help_text=_("Unique device identifier"),
        max_length=150, null=True
    )
    last_used = models.DateTimeField(null=True, blank=True)

    @classmethod
    def remove_sessions(cls, user_id, exclude=None):
        if exclude is None:
            exclude = []
        return cls.objects.filter(
            user_id=user_id
        ).exclude(
            key__in=exclude
        ).delete()
