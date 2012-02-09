from django.db import models

# Create your models here.
class Icontype(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    
class Icons(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    typeid = models.ForeignKey(Icontype)