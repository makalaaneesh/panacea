from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
	context = {}
	return render(request, 'main/index.html', context)

def home(request):
	paintings = Painting.objects.all()
	context = {'paintings' : paintings}
	return render(request, 'main/about.djt', context)


def listing(request):
	paintings = Painting.objects.all()
	context = {'paintings' : paintings}
	return render(request, 'main/listing.djt', context)