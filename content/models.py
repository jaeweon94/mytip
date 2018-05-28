from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
# Create your models here.


class Content(models.Model):

    category = models.CharField(max_length=100,choices = (
              ('1', '자기소개서'),
              ('2', '합격수기'),
              ('3', '대학생활'),
              ('4', '영어'),
              ('5', '돈 버는 방법'),
              ('6', '마케팅'),
              ('7', '독후감'),
              ('8', '성공 이야기'),
              ('9', '심리 상담'),
    ))

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=40)
    content = models.TextField()
    file_upload = models.FileField(blank=True, upload_to = 'admin/%Y/%m/%d')

    point = models.CharField(max_length=10)
    score = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add 최초에만
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
      return reverse('content:content_detail', args=[self.id])

