from django.contrib.auth import get_user_model

from hospital.commons.serializer import DynamicFieldsModelSerializer

USER = get_user_model()


class UserRegistrationSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = USER
        fields = USER.REGISTRATION_FIELDS
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def to_internal_value(self, data):
        # Added this cause phone-end can send empty string in DateField
        # Problem like these must be handled in phone-end
        # handling it in backend is not a good practice
        for _field in ('date_of_birth', 'phone_number'):
            if data.get(_field) == "":
                data[_field] = None
        return super().to_internal_value(data)

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = super().create(validated_data)
        instance.set_password(password)
        instance.save()
        return instance
