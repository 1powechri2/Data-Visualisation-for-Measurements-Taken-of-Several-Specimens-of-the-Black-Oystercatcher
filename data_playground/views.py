from django.shortcuts import render
from django.http import HttpResponse
from .models import BlackOystercatcher
from django.template import loader
from django_pandas.io import read_frame

def index(request):
    boyds = BlackOystercatcher.objects.all()
    df = read_frame(boyds)
    template = loader.get_template('data_playground/index.html')
    context = { 'boyds' : boyds,
              'df' : df }
    return HttpResponse(template.render(context, request))
