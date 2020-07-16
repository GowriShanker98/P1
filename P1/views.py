from django.http import HttpResponse

#create your views here.
def index(request):
    return HttpResponse('Hello World')


def home(request):
    return HttpResponse('<h1>Welcome to Home Page</h1>')
