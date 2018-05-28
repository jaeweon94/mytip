from django.db import models
from django.conf import settings
# Create your models here.


class Register(models.Model):

    YES_OR_NO = (
        ('Y', '예'),
        ('N', '아니오'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=40)
    content = models.TextField()
    file_upload = models.FileField(blank=True, upload_to='user/%Y/%m/%d')

    phone_number = models.CharField(max_length=20)
    kakao_id = models.CharField(max_length=20)
    bank = models.CharField(max_length=10)
    account_number = models.CharField(max_length=30)
    real_name = models.CharField(max_length=10)
    agree = models.CharField(max_length = 5, choices= YES_OR_NO, default= 'N')