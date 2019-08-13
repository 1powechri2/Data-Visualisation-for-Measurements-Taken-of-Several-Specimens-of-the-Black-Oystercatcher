from django.shortcuts import render
from django.http import HttpResponse
from .models import BlackOystercatcher
from django.template import loader

def index(request):
    boyds = BlackOystercatcher.objects.all()
    template = loader.get_template('data_playground/index.html')
    context = { 'boyds' : boyds }
    return HttpResponse(template.render(context, request))
