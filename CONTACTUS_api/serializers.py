from rest_framework import serializers
from shift_ev.addonsapp import models

class contact_usSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.contact_us
        fields = "__all__"
