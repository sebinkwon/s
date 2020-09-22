from django.db import models

import random

# Create your models here.

class star(models.Model):
    name = models.CharField(max_length = 30, verbose_name = '이름')
    birth = models.DateField(verbose_name = '생년월일')
    job = models.CharField(max_length=30, verbose_name = '직업')
    debut = models.DateField(verbose_name = '데뷔')
    level = models.CharField(max_length=30, verbose_name = '학력')
    photo = models.ImageField(upload_to = 'photo/',verbose_name = '사진')
    refresh = models.IntegerField(default = 0, verbose_name = '접속횟수')

    def countup(self):
        self.refresh += 1
        self.save()
        return self.refresh
    
    class Meta:
        verbose_name_plural = 'star'

    # def __str__(self):
    #     return 'No : %d , Name : %s' % (self.number, self.name)
