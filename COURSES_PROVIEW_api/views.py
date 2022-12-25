from django.shortcuts import render
from api_system import models
from api_system import serializers
from rest_framework.settings import api_system
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,status,filters

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'category_id', 'updated_at', 'language',)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

class InsturctorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.InsturctorSerializer
    queryset = models.Insturctor.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
