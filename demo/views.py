from urllib import request

from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get['username']
        password = request.POST.get['password']
        if username == 'admin' and password == '<PASSWORD>':
            return redirect('index.html')


def index(request):
    return render(request, 'index.html')
