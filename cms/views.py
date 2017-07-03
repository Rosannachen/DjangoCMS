# _*_ coding:utf8 _*_
import datetime

from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import UserCMS

# Create your views here.

# def welcome(request):
#     nowtime = datetime.datetime.now()
#     return render(request, "welcome.html", {
#         "nowtime": nowtime  # 模板变量
#     })

class welcomeview(View):
    def get(self, request):
        nowtime = datetime.datetime.now()
        return render(request, "welcome.html", {
            "nowtime": nowtime  # 模板变量
    })

    def post(self, request):
        pass


def index(request):
    if request.method == "POST":
        username = request.POST.get("username", "")  # 获取username关键字的词，若获取不到则默认为空
        password = request.POST.get("password", "")
        user_cms = UserCMS()  # 创建用户实例
        user_cms.username = username  # 为用户属性赋值
        user_cms.password = password  # 为密码属性赋值
        user_cms.save()  # 保存到数据库
        return HttpResponseRedirect(reverse("list"))  # 将处理重定向到用户列表页面（并继续处理）
    else:
        return render(request, "index.html", {})  # 正常get访问，返回主页


def list(request):
    all_user = UserCMS.objects.all()  # 获取所有用户对象
    return render(request, "list.html", {
        "all_user": all_user,  # 传递模板变量给html
    })


def delete(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        deluser = UserCMS.objects.filter(username=username, password=password)  # 查询要删除的用户记录
        deluser.delete()    # 执行删除方法
        return HttpResponseRedirect(reverse("list"))
    else:
        return render(request, "index.html", {})


def logout(request):
    nowtime = datetime.datetime.now()
    return render(request, "logout.html", {
        "nowtime": nowtime
    })