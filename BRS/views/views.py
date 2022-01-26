import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import *

def homepage(request):
    if request.session.get('is_login', None):
        username = request.session['username']
        return render(request, 'homepage.html', {'username':username})
    else:
        return render(request, 'homepage.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        userPhone = request.POST.get('userPhone', '')
        userEmail = request.POST.get('userEmail', '')
        userMajor = request.POST.get('userMajor', '')
        userGrade = request.POST.get('userGrade', '')
        userGender = request.POST.get('userGender', '')
        # print(username, password, userPhone, userEmail, userMajor, userGrade, userGender)
        UserInfo.objects.create(username=username, password=password, userPhone=userPhone,
                                userEmail=userEmail,userMajor=userMajor,userGrade=userGrade,userGender=userGender)
        return HttpResponseRedirect('/XJTU/homepage/')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'error': 0})

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        info = UserInfo.objects.filter(username=username)
        password = None
        for p in info:
            password=p.password
        password_given = request.POST.get('password', '')
        print(username, password, password_given)
        if username and password==password_given:
            request.session['is_login'] = '1'
            request.session['username'] = username
            return HttpResponseRedirect('/XJTU/homepage/')
        else:
            return render(request, 'login.html', {'error': 1})


def logout(request):
    request.session.clear()
    return HttpResponseRedirect('/XJTU/homepage')

def search(request):
    bookInfo = request.POST.get('search_text', '')
    # headers = {
    #     'content-type': 'application/json',
    #     'Referer': 'https://servicewechat.com/wx2f9b06c1de1ccfca/82/page-frame.html',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
    # }
    # apiKey = "0ac44ae016490db2204ce0a042db2916"
    # start = 0
    # count = 20
    # url = 'https://frodo.douban.com/api/v2/search/weixin?q={}&start={}&count={}&apiKey={}'.format(bookInfo, start, count,
    #                                                                                               apiKey)
    # r = requests.get(url, headers=headers)
    # content = r.json()
    # print('------------this is content-----------')
    # print(content)
    return render(request, 'search.html', {'username': request.session.get('username', None)})