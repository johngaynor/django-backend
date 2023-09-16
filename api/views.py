from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> returns response (request handler, action)


def say_hello(request):
    return HttpResponse('Hello world')


def home(request):
    return render(request, 'hello.html', {'name': 'John'})