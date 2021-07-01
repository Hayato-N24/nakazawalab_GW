from django.db import models

# Create your models here.

class UserInfo(models.Model):
    userName = models.CharField(max_length=200)
    allergy = models.CharField(max_length=200, null=True)
    like = models.CharField(max_length=200, null=True)
    dislike = models.CharField(max_length=200, null=True)
    