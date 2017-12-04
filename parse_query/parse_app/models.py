# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here. 


#Document model which has the file to be uploaded
class Document(models.Model):
    docfile = models.FileField(upload_to='uploads')
   
#Variable model which shows the format of how variables are stored with year and value
class Variable(models.Model):
    var=models.CharField(max_length=100)
    year=models.IntegerField()
    value=models.FloatField()
    
    
#Queryset model which forms the primary key identifier as they should make the query unique    
class Queryvar(models.Model):
    var=models.CharField(max_length=100)
    year=models.IntegerField()
    
    
   
    
 
    
    


