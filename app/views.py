from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('this is my first view function based view')
def dhoni(request):
    return HttpResponse('<h1>dhoni is best captain</h1>')
