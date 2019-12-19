from django.shortcuts import render
from .models import User
from django.http import JsonResponse


# app-response
def app_response(code=-1, data=None, error=''):
    response = {'code': code, 'data': data, 'error': error}
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


# 首页
def index(request):
    return render(request, template_name='app/index.html')


# 登录
def login(request):

    if not request.POST:
        return app_response(error='请输入手机号')
    phone = request.POST['phone']
    password = request.POST['password']
    if not phone or not password:
        return app_response(error='请输入用户名或密码')
    try:
        user = User.objects.get(phone=phone)
    except (KeyError, User.DoesNotExist):
        return app_response(error='手机号未注册')
    else:
        if user.password != password:
            return app_response(error='密码输入错误！')
        return app_response(code=0, data=user.to_dict())


# 注册
def register(request):

    if not request.POST:
        return app_response(error='请输入用户名')
    phone = request.POST['phone']
    password = request.POST['password']
    password2 = request.POST['password2']
    if not phone:
        return app_response(error='请输入手机号')
    if not password:
        return app_response(error='请输入密码')
    if password != password2:
        return app_response(error='两次输入的密码不一致')
    try:
        User.objects.get(phone=phone)
    except (KeyError, User.DoesNotExist):
        user = User(phone=phone, password=password)
        user.save()
        return app_response(code=0, data=user.to_dict())
    else:
        return app_response(error='手机号已被注册')
