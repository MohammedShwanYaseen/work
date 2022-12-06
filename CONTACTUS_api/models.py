from django.db import models
from functools import partial
from shift_ev.services.helpers import file_upload

class contact_us(models.Model):
    name =models.charfield(max_length=20,null=False)
    your_email = models.CharField(max_length=20,null=False,unique=True)
    phone_number = models.CharField(max_length=15,null=False,unique=True)
    your_message =models.textfield(max_length=225,null=False)
