from rest_framework import serializers
from .models import UserProfile
from .utils import is_valid_cell_phone

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserProfile model.
    """

    class Meta:
        model = UserProfile
        fields = '__all__'

    def validate_phone_number(self, value):
        """
        Custom validation for the 'phone_number' field using the utility function.
        """
        if not is_valid_cell_phone(value):
            raise serializers.ValidationError('Invalid phone number. Please enter a valid cell phone number.')

        return value
