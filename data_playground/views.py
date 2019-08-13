from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(
    "<h1>LET'S GET SOME DATA</h1>"
    )
