from django.utils import timezone
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework import status

from hospital.authentication.api.v1.serializers.token import CustomAuthTokenSerializer
from hospital.authentication.auth import CustomTokenAuthentication
from hospital.authentication.models import AuthToken


class ObtainAuthTokenView(ObtainAuthToken):
    authentication_classes = [CustomTokenAuthentication]
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = CustomAuthTokenSerializer(data=request.data,
                                               context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            device_id = self.request.headers.get('Device-ID')
            # if device id is None, null will be set to Authtoken' device_id
            token = AuthToken.objects.create(user=user, device_id=device_id)

            # to determine if it is user's first login
            user.last_login = timezone.now()
            user.save(update_fields=['last_login'])

            return Response(
                {
                    'token': token.key,
                    'available_tokens': AuthToken.objects.filter(user=user).count(),
                }
            )
        else:
            _response = serializer.errors
        return Response(_response, status=status.HTTP_400_BAD_REQUEST)


class DeleteAuthToken(APIView):
    """
    Delete user's AuthToken for a device
    """

    def post(self, request):
        device_id = self.request.headers.get('Device-ID')
        request.user.auth_tokens.filter(device_id=device_id).delete()
        return Response({"detail": "Logout successful"})
