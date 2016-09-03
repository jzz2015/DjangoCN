from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'user/index.html')

def writeblog(request):
    return render(request, 'user/writeblogs.html')

def viewblog(request):
    return render(request, 'user/viewblog.html')