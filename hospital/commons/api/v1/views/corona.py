from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from hospital.commons.api.v1.serializers import corona
from hospital.commons.api.v1.serializers.corona import CoronaSerializers
from hospital.commons.models import Corona


class coronaViewSet(viewsets.ModelViewSet):
    queryset = Corona.objects.all()
    serializer_class = CoronaSerializers
    permission_classes = [AllowAny]

