from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from hospital.core.api.v1.serializers.hospitals import HospitalSerializer, IcuBedSerializers, NormalBedSerializers, \
    VentilatorsBedSerializers
from hospital.core.models import hospitals, icu_bed, normal_bed, ventilators


class hospitalViewSet(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer
    queryset = hospitals.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class IcuBedViewSet(viewsets.ModelViewSet):
    serializer_class = IcuBedSerializers
    queryset = icu_bed.objects.all()


class NormalBedViewSet(viewsets.ModelViewSet):
    serializer_class = NormalBedSerializers
    queryset = normal_bed.objects.all()


class VentilatorsBedViewSet(viewsets.ModelViewSet):
    serializer_class = VentilatorsBedSerializers
    queryset = ventilators.objects.all()
