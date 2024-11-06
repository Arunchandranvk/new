from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import timedelta
from django.utils import timezone
from .validators import *
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None , **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone=models.BigIntegerField(unique=True,validators=[validate_phone])
    place = models.CharField(max_length=100)
    pincode=models.PositiveIntegerField(validators=[validate_pincode])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'place','phone','pincode']

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def _str_(self):
        return self.email



class Products(models.Model):
    name=models.CharField(max_length=100,unique=True)
    image=models.ImageField(upload_to="Product_Images",null=True)
    description=models.TextField(null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()  
    category=models.CharField(max_length=50,null=True)  
    created_at=models.DateTimeField(auto_now_add=True)  
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_image_url(self):
        base_url = "https://freeapi.luminartechnohub.com/"
        if self.image:
            return f"{base_url}{self.image.url}"
        return None