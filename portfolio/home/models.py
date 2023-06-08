from django.db import models

# Create your models here.
class Home(models.Model):
    course=models.CharField(max_length=255)
    place=models.CharField(max_length=255)
    cgpa=models.FloatField()