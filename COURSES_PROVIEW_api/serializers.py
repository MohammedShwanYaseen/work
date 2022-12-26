from rest_framework import serializers
from COURSES_PROVIEW_api import models


class CategoryConfigSerializer(serializers.ModelSerializer):
      class Meta:
           model = models.CategoryConfig
           fields ="_all_"



class InsturctorConfigSerializer(serializers.ModelSerializer):
      class Meta:
           model = models.InsturctorConfig
           fields ="_all_"


class CourseConfigSerializer(serializers.ModelSerializer):
      class Meta:
           model = models.CourseConfig
           fields ="_all_"
