from django.db import models

class UserInfo(models.Model):
    username= models.CharField(max_length=100)
    mailaddress= models.EmailField()
    selfIntroduction= models.CharField(max_length=200)
    allergie= models.CharField(max_length=200)

