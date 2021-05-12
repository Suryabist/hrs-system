from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters


from hospital.core.api.v1.serializers.hospitals import HospitalSerializer, IcuBedSerializers, NormalBedSerializers, \
    VentilatorsBedSerializers, OxygenCylindersSerializers, DeathSerializer, DischargeSerializer
from hospital.core.models import hospitals, icu_bed, normal_bed, ventilators, OxygenCylinders, death, discharge


class hospitalViewSet(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer
    queryset = hospitals.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['$name']




class IcuBedViewSet(viewsets.ModelViewSet):
    serializer_class = IcuBedSerializers
    queryset = icu_bed.objects.all()


class NormalBedViewSet(viewsets.ModelViewSet):
    serializer_class = NormalBedSerializers
    queryset = normal_bed.objects.all()


class VentilatorsBedViewSet(viewsets.ModelViewSet):
    serializer_class = VentilatorsBedSerializers
    queryset = ventilators.objects.all()


class OxygenBedViewSet(viewsets.ModelViewSet):
    serializer_class = OxygenCylindersSerializers
    queryset = OxygenCylinders.objects.all()


class DeathViewSet(viewsets.ModelViewSet):
    "API to crud the death details"
    serializer_class = DeathSerializer
    queryset = death.objects.all()


class DischargeViewSet(viewsets.ModelViewSet):

    "API to crud the Discharge details"

    serializer_class = DischargeSerializer
    queryset = discharge.objects.all()
