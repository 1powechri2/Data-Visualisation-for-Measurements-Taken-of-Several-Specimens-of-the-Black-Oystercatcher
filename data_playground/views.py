from django.shortcuts import render
from django.http import HttpResponse
from .models import BlackOystercatcher
from django.template import loader
from django_pandas.io import read_frame
import json

def index(request):
    boyds = BlackOystercatcher.objects.all()
    df = read_frame(boyds)
    ids = df['bird_id']
    data = df.head(0)
    template = loader.get_template('data_playground/index.html')
    context = {
              'props' : json.dumps(ids.tolist()),
              'df' : df,
              'data' : data,
              'ids' : ids
              }
    return HttpResponse(template.render(context, request))
