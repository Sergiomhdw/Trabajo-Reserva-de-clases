from django.shortcuts import render, HttpResponse
from django.template import Template, Context
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "app/login.html")

@login_required
def ramas(request):
    return render(request, "app/ramas.html")


