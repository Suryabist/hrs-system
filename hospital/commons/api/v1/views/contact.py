from rest_framework import viewsets

from hospital.commons.api.v1.serializers.contact import ContactSerializer
from hospital.commons.models import contact


class ContactViewSet(viewsets.ModelViewSet):
    queryset = contact.objects.all()
    serializer_class = ContactSerializer

