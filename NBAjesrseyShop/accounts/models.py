from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True
  
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser): 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

class Address(models.Model):
    country = models.CharField(max_length=50)    
    zip_code = models.CharField(max_length=50)
    city = models.CharField(max_length=50) 
    street = models.CharField(max_length=50)
    house_no = models.CharField(max_length=10)
    apartment_no = models.CharField(max_length=10, 
                                    blank=True, null=True)
    default_shipping_address = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='addresses', null=False)
    
    def __str__(self) -> str:
        return f'{self.country}, {self.city}, {self.zip_code}, {self.street}, {self.house_no}/{self.apartment_no}'
