from django.db import models

# Create your models here.
class User(models.Model):
    armyno = models.CharField(max_length=15)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    posttype = models.CharField(max_length=20)
    relation = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    rank = models.TextField(max_length=20)
    healthproblem = models.TextField(max_length=100)
    problemhistory = models.TextField(max_length=100)        
    
class Analyze(models.Model):
    images = models.ImageField(upload_to='images/%Y/%m/%d/', max_length=255, null=True, blank=True)    