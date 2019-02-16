from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
  return HttpResponse("Hello django")

def time(request):
  now = datetime.now()
  return render(request,'homepage/index.html', {'now': now })
  #using render method from shortcuts module return render(request,'homepage/index.html', {'now': now })#
  #using render_to_response from shortcuts module(NOTE:Its depricated now) return render_to_response('homepage/index.html', {'now': now })#