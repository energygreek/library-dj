from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse

from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    name = request.user.username
    return render(request, 'home/index.html',{'name':name})

def register(request):
    user = User.objects.create_user(username='123', email='', password='123')
    user.save()

def login(request):
    if request.method == 'GET':
        return render(request, 'home/login.html')

    if request.method == 'POST':
        # 如果登录成功，绑定参数到cookie中，set_cookie
        username = request.POST.get('username')        
        password = request.POST.get('password')  
        user = auth.authenticate(username=username, password=password)
        #2、进行登录，django 提供 login 将用户信息保存到会话中
        if user:
            auth.login(request, user)
            if user.is_staff:
                return HttpResponseRedirect(reverse('home:operator'))
            else:
                return HttpResponseRedirect(reverse('home:reader'))
        else:
            return render(request, "home/login.html")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home:index'))

def operator(request):
    name = request.user.username
    return render(request, 'home/operator.html',{'name':name})

def reader(request):
    name = request.user.username

    
    # 查询出所借图书
    return render(request, 'home/reader.html',{'name':name})