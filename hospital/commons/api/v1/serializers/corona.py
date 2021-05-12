from rest_framework import serializers

from hospital.commons.models import Corona


class CoronaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Corona
        fields = "__all__"
