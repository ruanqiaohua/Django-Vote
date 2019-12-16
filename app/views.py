from django.shortcuts import render
from .models import User


def index(request):
    return render(request, template_name='app/index.html')


def login(request):
    if not request.POST:
        return render(request, template_name='app/login.html')
    phone = request.POST['phone']
    password = request.POST['password']
    try:
        user = User.objects.get(phone=phone, password=password)
    except (KeyError, User.DoesNotExist):
        return render(request, template_name='app/login.html', context={'error_message': '手机号未注册'})
    else:
        return render(request, template_name='app/userInfo.html', context={'user': user})


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
