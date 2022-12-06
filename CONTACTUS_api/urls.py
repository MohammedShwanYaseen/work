from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()

urlpatterns = [

    path("contact-us/", views.contact_usView.as_view(), name="contact_us"),

    path("", include(router.urls)),
]
