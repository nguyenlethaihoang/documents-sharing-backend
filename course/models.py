from email.policy import default
from operator import mod
from django.db import models
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    content = models.CharField(max_length=255)


class Major(models.Model):
    # id = models.IntegerField(primary_key=True,max_length=100)
    name = models.CharField(max_length=255) 

class Subject(models.Model):
    # id = models.IntegerField(primary_key=True,max_length=255)
    name = models.CharField(max_length=255) 
    majorID = models.IntegerField(max_length=100)
    imgUrl = models.CharField(max_length=255, default='') 


class User(models.Model):
    # id = models.IntegerField(primary_key=True,max_length=255)
    studentID = models.CharField(max_length=10) 
    name = models.CharField(max_length=255) 
    permisson = models.IntegerField(default=1, max_length=3)

class Document(models.Model):
    # id = models.IntegerField(primary_key=True,max_length=10000)
    name = models.CharField(max_length=255) 
    description = models.CharField(max_length=255)
    # 1: pending
    # 2: authorize
    # 3: unauthorize
    status = models.IntegerField(default=1, max_length=3)
    # 1: slide
    # 2: mid-term
    # 3: final-term
    type = models.IntegerField(default=1, max_length=100)
    link = models.CharField(max_length=255) 
    date = models.CharField(max_length=10) 
    size = models.CharField(max_length=10) 
    subjectID = models.CharField(max_length=100) 
    userID = models.CharField(max_length=100)
    imgUrl = models.CharField(max_length=255, default='https://vcdn1-vnexpress.vnecdn.net/2019/06/04/Hoa1-6179-1559618180.jpg?w=0&h=0&q=100&dpr=2&fit=crop&s=L1c433SwHnT3vn1ZPXOhyQ') 
