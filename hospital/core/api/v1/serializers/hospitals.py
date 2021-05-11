from rest_framework import serializers

from hospital.core.models import hospitals, icu_bed, normal_bed, ventilators, OxygenCylinders, discharge, death


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


class OxygenCylindersSerializers(serializers.ModelSerializer):
    class Meta:
        model = OxygenCylinders
        fields = '__all__'


class DischargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = discharge
        fields = '__all__'


class DeathSerializer(serializers.ModelSerializer):
    class Meta:
        model = death
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    # icu = IcuBedSerializers(many=True, )
    # normal = NormalBedSerializers(many=True, )
    # ventilators = VentilatorsBedSerializers(many=True, )

    class Meta:
        model = hospitals
        fields = '__all__'
