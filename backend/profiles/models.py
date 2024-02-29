from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .utils import is_valid_cell_phone

class UserProfile(models.Model):
    # Fields for user profile information
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    class Meta:
        app_label = 'profiles'

    def __str__(self):
        # String representation of the user profile
        return f"{self.first_name} {self.surname}"
    
    def clean(self):
        # Override the clean method to perform additional validation
        super().clean()
        self.validate_phone_number()

    def validate_phone_number(self):
        # Custom validation using the utility function
        if not is_valid_cell_phone(self.phone_number):
            # Raise validation error if the phone number is not valid
            raise ValidationError(
                _('Invalid phone number. Please enter a valid cell phone number.'),
                code='invalid_phone_number'
            )
