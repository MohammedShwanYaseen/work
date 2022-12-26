from django.contrib import admin
from COURSES_PROVIEW_api import models


admin.site.register(models.Course)
admin.site.register(models.Category)
admin.site.register(models.Insturctor)
