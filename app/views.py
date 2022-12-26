from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def lavanya(request):
    return HttpResponse('lavanya is good girl')
def sukanya(request) :
    return HttpResponse('sukanya is a my best friend')  
def radha(request):
    return HttpResponse('<h1>radha is beautiful girl</h1')     