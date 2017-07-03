# _*_ coding:utf8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserCMS(models.Model):
    username = models.CharField(verbose_name="姓名", max_length=50)
    password = models.CharField(verbose_name="密码", max_length=50)

    class Meta:
        verbose_name = "用户CMS"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
