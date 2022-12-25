from django.contrib import admin
from shift_ev.career_App import models


@admin.register(models.Course)
class TeamAdmin(admin.ModelAdmin):
    list_display =("Category_name","available_language","Insturctor_name","course_description","over_view")


@admin.register(models.Category)
class CareerAdmin(admin.ModelAdmin):
    list_display =("category_id","Course_name","Insturctor_courses","details","price","updated_at","created_at","language","book_live_session")

@admin.register(models.Insturctor)
class CareerAdmin(admin.ModelAdmin):
    list_display =("Insturctor_name","image","description","NumOfStudent","Insturctor_rate","Insturctor_courses")
