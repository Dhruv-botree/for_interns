from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
# Create your models here.


class User(AbstractUser):
    def __str__(self):
        return self.username
    region = models.CharField(max_length=120)

class Facility(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=120)

class House(models.Model):
    def __str__(self):
        return self.owner.username+"_"+self.address
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="houses")
    address = models.TextField()
    facilities = models.ManyToManyField(Facility,related_name="facilities")
    value = models.FloatField(null=True,validators=[MinValueValidator(0)])