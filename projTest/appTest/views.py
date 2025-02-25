from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Person


# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    persons = Person.objects.all().values('id','firstname')
    context = {
        'persons': persons
    }
    return HttpResponse(template.render(context, request))

def details(request,id):
    template = loader.get_template('details.html')
    persons = Person.objects.get(id=id)
    context = {
        'persons': persons
    }
    return HttpResponse(template.render(context, request))