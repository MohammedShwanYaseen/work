from django.db import models

class Category(models.Model):
    id =  models.IntegerField(primary_key= True)
    name = models.CharField(max_length = 100)

class Course(models.Model):
    id =  models.IntegerField(primary_key= True)
    category_id = models.ForeignKey(Category,null=True, on_delete = models.SET_NULL)
    name = models.CharField(max_length = 150)
    details = models.CharField(max_length =1000)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length =50)


class CourseImage(models.Model):
     id = models.IntegerField(primary_key= True)
     image_path = models.TextField()
     course_id = models.ForeignKey(Course, null=True , on_delete=models.SET_NULL)


class CourseVideo(models.Model):
     id = models.IntegerField(primary_key= True)
     video_path = models.TextField()
     course_id = models.ForeignKey(Course, null=True , on_delete=models.SET_NULL)
     name = models.CharField(max_length=100)
     description = models.TextField()


class Insturctor(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=100)
    image = models.TextField()
    description = models.TextField()

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


#class related_courses(models.Model):

#class coursepreview(models.Model):

course_video
