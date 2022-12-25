from rest_framework import serializers
from CONTACTUS_api import models

class contact_usSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.contact_us
        fields = "__all__"
