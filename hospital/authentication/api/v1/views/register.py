from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from hospital.authentication.api.v1.serializers.register import UserRegistrationSerializer


class UserRegistrationView(CreateAPIView):
    """
        View for registering user
    """

    serializer_class = UserRegistrationSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # building response dict
        response_dict = {"detail": "An account has been created successfully.",
                         }

        return Response(response_dict,
                        status=status.HTTP_201_CREATED,
                        headers=headers)
