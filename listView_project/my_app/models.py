from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name
  
# No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
#  this function is to solve above error
    def get_absolute_url(self):
        return reverse("base_app:detail", kwargs={"pk": self.pk})


 

class student(models.Model):
    name = models.CharField(max_length=256)
    age =models.PositiveIntegerField()
    school =models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    #  function return after add student
    def get_absolute_url(self):
        return reverse("base_app:detail", kwargs={"pk": self.pk})