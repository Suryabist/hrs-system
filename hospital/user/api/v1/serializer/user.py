from django.contrib.auth import get_user_model

from hospital.commons.serializer import DynamicFieldsModelSerializer

USER = get_user_model()


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = USER
        fields = ['email', 'first_name', 'last_name', 'password', 'hospital', 'phone_number']

    def to_internal_value(self, data):
        # Added this cause phone-end can send empty string in DateField
        # Problem like these must be handled in phone-end
        # handling it in backend is not a good practice
        for _field in ('hospital', 'phone_number'):
            if data.get(_field) == "":
                data[_field] = None
        return super().to_internal_value(data)