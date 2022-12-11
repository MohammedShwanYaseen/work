from django.db import models



class Category(models.Model):
    category_id =  models.IntegerField(primary_key= True)
    name = models.CharField(max_length = 100,null=False)
    language = models.CharField(max_length =50,null=False)
    available_language =
    Insturctor_name = models.foreignkey(Insturctor,null=False)
    course_description = models.TextField()
    over_view = models.TextField()



class chapters(models.Model):
    chapter_id = models.IntegerField(primary_key= True)
    chapter_name = odels.CharField(max_length = 150,null=False)
    chapters =

class session_summary(models.Model):
    session_summary_id = models.IntegerField(primary_key= True)
    note =
    noteImag =

class attached_files(models.Model):
    attached_files_id = models.IntegerField(primary_key= True)
    files = models.FileField(null=True,upload_to='files')


class book_live_session(models.Model):
    book_live_session_id =models.IntegerField(primary_key=True)
    book = models.FileField(null=True,upload_to='book') 


class Course(models.Model):
    Course_id =  models.IntegerField(primary_key= True)
    category_id = models.ForeignKey(Category,null=False, on_delete = models.SET_NULL)
    Course_name = models.CharField(max_length = 150)
    details = models.CharField(max_length =1000)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length =50)


class CourseImage(models.Model):
     id = models.IntegerField(primary_key= True)
     image_course = models.ImageField(upload_to ='uploads/')
     course_id = models.ForeignKey(Course, null=True , on_delete=models.SET_NULL)


class Insturctor(models.Model):
    Insturctor_id = models.IntegerField(primary_key= True)
    Insturctor_name = models.CharField(max_length=100)
    image = models.TextField()
    description = models.TextField()
    #NumOfStudent =
    #Insturctor_rate =
    #Insturctor_courses =

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
