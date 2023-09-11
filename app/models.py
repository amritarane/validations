from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=100)
    sid=models.IntegerField()
    sage=models.IntegerField()
    semail=models.EmailField()
    sremail= models.EmailField()
    botcatcher=models.CharField(max_length=100)