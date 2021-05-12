from rest_framework import serializers

from hospital.commons.models import contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = "__all__"
