from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from hospital.commons.api.v1.serializers.contact import ContactSerializer
from hospital.commons.models import contact


class ContactViewSet(viewsets.ModelViewSet):
    queryset = contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

