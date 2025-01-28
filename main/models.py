from django.db import models
from rest_framework import serializers

# Create your models here.
class Bookmark(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    url = models.URLField(max_length=200)
    image_url = models.URLField(max_length=200) 
    description = models.TextField(null=True, blank=True)
    
