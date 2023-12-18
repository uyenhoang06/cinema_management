from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('Enter a valid email'))

    def create_user(self, first_name, last_name, email, phone, password, address, gender, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Email is required'))

        if not first_name:
            raise ValueError(_('First name is required'))

        if not last_name:
            raise ValueError(_('Last name is required'))

        if not phone:
            raise ValueError(_('Phone is required'))

        if not address:
            raise ValueError(_('Address is required'))

        if not gender:
            raise ValueError(_('Gender is required'))

        user = self.model(first_name=first_name, last_name= last_name, email= email, phone= phone, address= address, gender= gender, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, phone, password, address, gender, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_verified', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('is_superuser must be true'))

        user = self.create_user(
            first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, gender=gender, **extra_fields
        )
        user.set_password(password)

        user.save(using=self._db)
        return user


