from django.http import HttpResponse
from django.shortcuts import render

#create your views here.
def index(request):
    return HttpResponse('Hello World')

def home(request):
    return HttpResponse('<h1>Welcome to Home Page</h1>')

def html_demo1(request):
    return render(request,"sample.html")

def html_demo2(request):
    return render(request,"sample1.html")