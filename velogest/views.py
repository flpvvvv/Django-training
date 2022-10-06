from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def ma_vue(request):
    return HttpResponse("Hello")