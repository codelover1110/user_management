from django.db import models
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    class Meta:
        app_label = 'profiles'

    def __str__(self):
        return f"{self.first_name} {self.surname}"
    
    def clean(self):
        super().clean()
        self.validate_phone_number()

    def validate_phone_number(self):
        if not re.match(r'^\+?1?\d{9,15}$', self.phone_number):
            raise ValidationError(
                _('Invalid phone number. Please enter a valid cell phone number.'),
                code='invalid_phone_number'
            )
