# _*_ coding:utf8 _*_
from django.contrib import admin
from models import UserCMS

# Register your models here.

class UserAdmin(admin.ModelAdmin):  # 创建模型管理类（继承自admin.ModelAdmin）
    pass

admin.site.register(UserCMS, UserAdmin) # 将模型与模型管理类进行注册


