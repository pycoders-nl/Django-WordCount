from django.db import models
from datetime import datetime

# Create your models here.

class Name(models.Model):
    def __str__(self):                               # baslik ve yazilari gostermek icin
        return self.header
    header = models.CharField(max_length=200)        # kisa birseyse CharField
    date_created = models.DateTimeField(default=datetime.now, blank=True)


class Text(models.Model):
    def __str__(self):
        return self.text
    text = models.TextField()                       # uzun birsey yazacaksak burasini kullaniyoruz
    date_created = models.DateTimeField("data_created")                    # olusturma tarihi

