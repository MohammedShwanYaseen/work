
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Insturctor(models.Model):

    IN_RATE_CHOICES=[
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
    ]

    Insturctor_name = models.CharField(max_length=100)
    Insturctor_image = models.ImageField(upload_to ='uploads/')
    description = models.TextField()
    NumOfStudent =models.IntegerField()
    Insturctor_rate = models.IntegerField(choices=IN_RATE_CHOICES)


class Category(models.Model):
        Category_name = models.CharField(max_length = 100,null=False)
        available_language =models.CharField(max_length =50,null=False)
        Insturctor = models.ForeignKey(Insturctor,null=True,on_delete=models.CASCADE)
        course_description = models.TextField()
        over_view = models.TextField()


class Course(models.Model):
        Category = models.ForeignKey(Category,null=True, on_delete = models.SET_NULL)
        image_course = models.ImageField(upload_to ='uploads/')
        Course_name = models.CharField(max_length = 150)
        instructor = models.ManyToManyField("Insturctor", related_name= 'courses')
        details = models.CharField(max_length =1000)
        price = models.IntegerField()
        updated_at = models.DateTimeField(auto_now=True)
        created_at = models.DateTimeField(auto_now_add=True)
        language = models.CharField(max_length =50)
        book_live_session = models.FileField(null=True,upload_to='book')


class session_summary(models.Model):
    note = models.TextField()
    noteImag =  models.ImageField(upload_to ='uploads/')

class attached_files(models.Model):
    files = models.FileField(null=True,upload_to='files')

class chapters(models.Model):
    Course = models.ForeignKey(Course, null=True, on_delete = models.SET_NULL)
    chapter_number = models.CharField(max_length = 2,null=False)
    chapter_name = models.CharField(max_length = 150,null=False)
    chapter_description = models.TextField(null = True)
    session_summary =models.ForeignKey(session_summary,null=True, on_delete = models.SET_NULL)
    attached_files =models.ForeignKey(attached_files,null=True,on_delete=models.SET_NULL)

class CourseVideo(models.Model):
    chapters = models.ForeignKey(chapters, null=True, on_delete=models.SET_NULL)
    video_course = models.FileField(upload_to='upload videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)

class reviews(models.Model):
    RATE_CHOICES=[
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
    ]
    #user =models.ForeignKey(user, on_delete=models.CASCADE)
    comment =models.TextField(max_length=300,blank=True)
    review_date = models.DateTimeField(auto_now = True)
    review_rate =models.IntegerField(choices=RATE_CHOICES)
