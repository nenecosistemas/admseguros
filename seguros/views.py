from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Template,Context
from .models import *
from .forms import AseguradoForm

# Create your views here.
def home(request):
    t = get_template('index.html')
    html = t.render()
    return HttpResponse(html)

def aseguradoform(request):
    form = AseguradoForm()
    context = {'form':form}  
         
    return render(request,'asegurado/aseguradoform.html', context )
