from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.expressions import F

# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField('customer status', default=False)
    is_shop = models.BooleanField('teacher status', default=False)
    contact_number = models.CharField(max_length=999, null=False)
    email = models.EmailField(unique=True)

class Customer(models.Model):
    last_name = models.CharField(max_length=99)
    first_name = models.CharField(max_length=99)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
