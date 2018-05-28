from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from content.models import Content
# Create your models here.


class Profile(models.Model):

    SEX_CHOICES = (
        ('M', '남성'),
        ('W', '여성'),
        )

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    sex = models.CharField(max_length=5, choices = SEX_CHOICES)
    year = models.CharField(max_length=10)
    job = models.CharField(max_length=10)
    point = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username