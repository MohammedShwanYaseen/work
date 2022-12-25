from django.urls import path, include
from rest_framework.routers import DefaultRouter
from COURSES_PROVIEW_api import views

router = DefaultRouter()
router.register('Course', views.CourseViewSet)
router.register('Category', views.CategoryViewSet)
router.register('Insturctor', views.InsturctorViewSet)


urlpatterns = [

    path('', include(router.urls))
]
