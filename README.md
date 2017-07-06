# DjangoCMS

1.使用migration功能，修改Model后可以在不影响现有数据的前提下重建表结构

python manage.py makemigrations

python manage.py migrate

2.修改setting.py

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','192.168.80.80','localhost'] ---> 可以访问网站的ip

3.运行程序

python manage.py runserver 0.0.0.0:8000
