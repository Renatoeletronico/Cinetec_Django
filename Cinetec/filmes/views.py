from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.messages import constants
from django.contrib import messages 
from django.contrib import auth


# Create your views here.

def home (request) :
    return render(request,'home.html')