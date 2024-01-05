from django.http import HttpResponse
from django.shortcuts import render
from . import views

# Create your views here.
def taskList(request):
   return HttpResponse("<h1>Hello Django</h1>")