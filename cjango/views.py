from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect

def index(request):
    return render(request, "index.html")

def chart(request):
    return render(request, "charts.html")