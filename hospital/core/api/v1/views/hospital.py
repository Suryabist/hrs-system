from rest_framework import viewsets

from hospital.core.api.v1.serializers.hospitals import HospitalSerializer
from hospital.core.models import hospitals


class hospitalViewSet(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer
    queryset = hospitals.objects.all()
