from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hi there')

def second_view(request):
    return HttpResponse('hi there')
