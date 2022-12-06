from django.contrib import admin
from shift_ev.addonsapp import models
from solo.admin import SingletonModelAdmin


@admin.register(models.contact_us)
class contact_usAdmin(admin.ModelAdmin):
    list_display = ("name","your_email ", "phone_number","your_message",)
