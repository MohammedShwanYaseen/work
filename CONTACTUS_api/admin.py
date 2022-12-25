from django.contrib import admin
from CONTACTUS_api import models



@admin.register(models.contact_us)
class contact_usAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone_number","message",)
