from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from hospital.commons.mixins.viewset import ListRetrieveUpdateViewSetMixin
from hospital.user.api.v1.serializer.user import UserSerializer

USER = get_user_model()


class UserViewSet(ListRetrieveUpdateViewSetMixin):
    """
            list: List of users

            update: Update User information, Current logged in user can use `me`

            partial_update: Update User information, Current logged in user can use `me`

            password: Change User password, Current logged in user can use `me`

            retrieve: retrieve user information, Current logged in user can use `me`

        """
    serializer_class = UserSerializer
    queryset = USER.objects.all()
    lookup_url_kwarg = 'username'
    lookup_field = 'username'

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_object(self):
        if self.kwargs['username'] == 'me':
            self.kwargs['username'] = self.request.user.username
        return super().get_object()

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        if self.action == 'retrieve':
            kwargs['fields'] = ['email', 'first_name', 'last_name', 'password', 'hospital', 'phone_number',
                                ]
        return serializer_class(*args, **kwargs)
