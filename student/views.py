from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to my website")

def add(request):
    return HttpResponse("Add student")

def remove(request):
    return HttpResponse("Remove Student")

def update(request):
    return HttpResponse("update student")