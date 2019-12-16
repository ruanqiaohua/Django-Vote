from django.shortcuts import render
from .models import User
from django.http import JsonResponse


# app-response
def app_response(code=-1, data={}, error=''):
    response = {'code': code, 'data': data, 'error': error}
    return response


# 首页
def index(request):
    return render(request, template_name='app/index.html')


# 登录
def login(request):

    if not request.POST:
        return JsonResponse(app_response(error='请输入用户名'))
    phone = request.POST['phone']
    password = request.POST['password']
    if not phone or not password:
        return JsonResponse(app_response(error='请输入用户名或密码'))
    try:
        user = User.objects.get(phone=phone, password=password)
    except (KeyError, User.DoesNotExist):
        return JsonResponse(app_response(error='手机号未注册'))
    else:
        return JsonResponse(app_response(code=0, data=user.to_dict()))


# 注册
def register(request):
    if not request.POST:
        return render(request, template_name='app/register.html')
    phone = request.POST['phone']
    password = request.POST['password']
    password2 = request.POST['password2']
    if not phone:
        return render(request, template_name='app/register.html', context={'error_message': '请输入手机号'})
    if not password:
        return render(request, template_name='app/register.html', context={'error_message': '请输入密码'})
    if password != password2:
        return render(request, template_name='app/register.html', context={'error_message': '两次输入的密码不一致'})
    try:
        User.objects.get(phone=phone)
    except (KeyError, User.DoesNotExist):
        user = User(phone=phone, password=password)
        user.save()
        return render(request, template_name='app/register.html', context={'loginSuc': "注册成功"})
    else:
        return render(request, template_name='app/register.html', context={'error_message': "手机号已被注册"})
