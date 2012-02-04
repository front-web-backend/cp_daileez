from django.db import models

# Create your models here.
class Icontype(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    
class Icons(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    typeid = models.ForeignKey(Icontype)