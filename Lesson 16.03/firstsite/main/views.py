from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("<h1> Wow! Hello World from WEB!! </h1>")


def JackPage(request):
    return HttpResponse("<h1> This is Jack Page!</h1>")