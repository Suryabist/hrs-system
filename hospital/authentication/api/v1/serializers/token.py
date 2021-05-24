from django.contrib.auth import get_user_model
from rest_framework.authtoken.serializers import AuthTokenSerializer

from hospital.core.api.v1.serializers.hospitals import HospitalSerializer


class CustomAuthTokenSerializer(AuthTokenSerializer):

    def validate(self, attrs):
        user = get_user_model().objects.filter(
            email__iexact=attrs['username']
        ).first()
        # to change the message as authenticate() method returns True or False only
        # and same message is returned
        data = super().validate(attrs)
        return data
