from rest_framework import serializers

from hospital.core.models import hospitals


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = hospitals
        fields = '__all__'
