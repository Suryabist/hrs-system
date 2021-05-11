from rest_framework import serializers

from hospital.core.models import hospitals, icu_bed, normal_bed, ventilators


class IcuBedSerializers(serializers.ModelSerializer):
    class Meta:
        model = icu_bed
        fields = '__all__'


class NormalBedSerializers(serializers.ModelSerializer):
    class Meta:
        model = normal_bed
        fields = '__all__'


class VentilatorsBedSerializers(serializers.ModelSerializer):
    class Meta:
        model = ventilators
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    # icu = IcuBedSerializers(many=True, )
    # normal = NormalBedSerializers(many=True, )
    # ventilators = VentilatorsBedSerializers(many=True, )

    class Meta:
        model = hospitals
        fields = '__all__'
