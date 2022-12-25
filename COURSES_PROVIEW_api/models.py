from django.db import models
from django.conf import api_system
from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework.authtoken.models import Token



class Category(models.Model):
    name = models.CharField(max_length = 100,null=False)
    language = models.CharField(max_length =50,null=False)
    #available_language =
    Insturctor_name = models.foreignkey(Insturctor,null=False)
    course_description = models.TextField()
    over_view = models.TextField()



class chapters(models.Model):
    chapter_number = models.CharField(max_length = 2,null=False)
    chapter_name = models.CharField(max_length = 150,null=False)
    Insturctor_name = models.foreignkey(Insturctor)
    chapter_description = models.textField(null = True)
    session_summary =models.foreignkey(session_summary,null=True)
    attached_files =models.foreignkey(attached_files,null=True , on_delete=models.SET_NULL)

class CourseImage(models.Model):
     image_course = models.ImageField(upload_to ='uploads/')
     course_id = models.ForeignKey(Course, null=True , on_delete=models.SET_NULL)

class CourseVideo(models.Model):
    video_course = models.VideoFild(upload_to ='uploads/')
    chapters = foreignkey(chapters,on_delete=models.SET_NULL)


class session_summary(models.Model):
    session_summary_id = models.IntegerField(primary_key= True)
    note = models.TextField()
    noteImag =  models.ImageField(upload_to ='uploads/')

class attached_files(models.Model):
    attached_files_id = models.IntegerField(primary_key= True)
    files = models.FileField(null=True,upload_to='files')


class Course(models.Model):

    category_id = models.ForeignKey(Category,null=False, on_delete = models.SET_NULL)
    Course_name = models.CharField(max_length = 150)
    Insturctor_courses = models.ForeignKey("Instructor")
    details = models.CharField(max_length =1000)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length =50)
    book_live_session = book = models.FileField(null=True,upload_to='book')


class Insturctor(models.Model):

    Insturctor_name = models.CharField(max_length=100)
    image = models.TextField()
    description = models.TextField()
    NumOfStudent =IntegerField()
    Insturctor_rate = model.positiveSmilIntgerField(choices=RATE_CHOICES)
     Insturctor_courses = models.ManyToManyField(Course)

RATE_CHOICES=[
(1,'1')
(2,'2')
(3,'3')
(4,'4')
(5,'5')
]

class reviews(models.Model):
user =models.foreignkey(user, on_delete=models.CASCADE)
comment =models.textField(max_length=300,blank=True)
review_date = models.DateTimeField(auto_new_add=True)
review_rate =model.positiveSmilIntgerField(choices=RATE_CHOICES)
