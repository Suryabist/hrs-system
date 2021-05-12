from rest_framework import serializers

from hospital.core.models import hospitals, icu_bed, normal_bed, ventilators, OxygenCylinders, discharge, death, \
    HduBeds, focalperson


class DeathSerializer(serializers.ModelSerializer):
    class Meta:
        model = death
        fields = '__all__'


class VentilatorsBedSerializers(serializers.ModelSerializer):
    class Meta:
        model = ventilators
        fields = '__all__'


class DischargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = discharge
        fields = '__all__'


class NormalBedSerializers(serializers.ModelSerializer):
    class Meta:
        model = normal_bed
        fields = [
            'capacity',
            'occupied',
            'available'
        ]


class OxygenCylindersSerializers(serializers.ModelSerializer):
    class Meta:
        model = OxygenCylinders
        fields = '__all__'


class IcuBedSerializers(serializers.ModelSerializer):
    class Meta:
        model = icu_bed
        fields = "__all__"


class hduBedSerializers(serializers.ModelSerializer):
    class Meta:
        model = HduBeds
        fields = "__all__"


class FocalPersonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = focalperson
        fields = "__all__"


class HospitalSerializer(serializers.ModelSerializer):
    normal = NormalBedSerializers()
    icu = IcuBedSerializers()
    discharge = DischargeSerializer()
    death = DeathSerializer()
    ventilators = VentilatorsBedSerializers()
    oxygen_plant = OxygenCylindersSerializers()
    hdu = hduBedSerializers()
    focalperson = FocalPersonsSerializers()

    class Meta:
        model = hospitals
        fields = 'name', 'address', 'hospital_type', 'phone_no', 'lat', 'long', 'normal', 'discharge', 'death', 'icu', 'ventilators', 'oxygen_plant', 'hdu', 'focalperson'
