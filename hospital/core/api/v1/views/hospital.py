from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny

from hospital.core.api.v1.serializers.hospitals import HospitalSerializer, IcuBedSerializers, NormalBedSerializers, \
    VentilatorsBedSerializers, OxygenCylindersSerializers, DeathSerializer, DischargeSerializer, hduBedSerializers, \
    FocalPersonsSerializers
from hospital.core.models import hospitals, icu_bed, normal_bed, ventilators, OxygenCylinders, death, discharge, \
    HduBeds, focalperson


class hospitalViewSet(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer
    queryset = hospitals.objects.all().order_by('icu__available')
    filter_backends = (filters.SearchFilter,)
    search_fields = ['^name']
    permission_classes = [AllowAny]


class IcuBedViewSet(viewsets.ModelViewSet):
    serializer_class = IcuBedSerializers
    queryset = icu_bed.objects.all()
    permission_classes = [AllowAny]


class NormalBedViewSet(viewsets.ModelViewSet):
    serializer_class = NormalBedSerializers
    queryset = normal_bed.objects.all()
    permission_classes = [AllowAny]


class VentilatorsBedViewSet(viewsets.ModelViewSet):
    serializer_class = VentilatorsBedSerializers
    queryset = ventilators.objects.all()
    permission_classes = [AllowAny]


class OxygenBedViewSet(viewsets.ModelViewSet):
    serializer_class = OxygenCylindersSerializers
    queryset = OxygenCylinders.objects.all()
    permission_classes = [AllowAny]


class DeathViewSet(viewsets.ModelViewSet):
    "API to crud the death details"
    serializer_class = DeathSerializer
    queryset = death.objects.all()
    permission_classes = [AllowAny]


class DischargeViewSet(viewsets.ModelViewSet):
    "API to crud the Discharge details"

    serializer_class = DischargeSerializer
    queryset = discharge.objects.all()
    permission_classes = [AllowAny]



class HduBedsViewSet(viewsets.ModelViewSet):
    serializer_class = hduBedSerializers
    queryset = HduBeds.objects.all()
    permission_classes = [AllowAny]


class FocalPersonViewSet(viewsets.ModelViewSet):
    serializer_class = FocalPersonsSerializers
    queryset = focalperson.objects.all()
    permission_classes = [AllowAny]
