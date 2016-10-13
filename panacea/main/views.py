from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

def index(request):
	context = {}
	return render(request, 'main/index.html', context)


def test(request):
	paintings = Painting.objects.all()
	categories = Category.objects.all()
	context = {'paintings' : paintings, 'categories':categories}
	return render(request, 'main/index2.html', context)

def home(request):
	paintings = Painting.objects.all()
	context = {'paintings' : paintings}
	return render(request, 'main/about.djt', context)


def listing(request):
	paintings = Painting.objects.all()
	context = {'paintings' : paintings}
	return render(request, 'main/listing.djt', context)

# @csrf_exempt
# def testview(request):
# 	if request.method == "POST":
# 		print request.POST
# 	return HttpResponse("ok")