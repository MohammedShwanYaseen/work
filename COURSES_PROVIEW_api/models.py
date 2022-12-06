from django.db import models

class Category(models.Model):
    """docstring fo Category."""

    def __init__(self, arg):
        supe Category, self).__init__()
        self.arg = arg

category_name = models.charfield(max_length=25,null=False)
category_date = models.DateTimeField(auto_new_add=True)
category_description =models.charfield(null=False)
instructor =models.charfield(max_length=25,null=False)
courses_by_instructor =
language =
Available_language =
course_description =models.charfield(null=False)
overview =models.charfield()

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
