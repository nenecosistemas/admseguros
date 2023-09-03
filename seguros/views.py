from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Template,Context

# Create your views here.
def inicio(request):
    t = get_template('index.html')
    html = t.render()
    return HttpResponse(html)
