from django.db import models
from functools import partial


class contact_us(models.Model):
    name =models.CharField(max_length=20,null=False)
    email = models.EmailField(null=False,unique=True)
    phone_number = models.CharField(max_length=15,null=False,unique=True)
    message =models.TextField(max_length=225,null=False)
