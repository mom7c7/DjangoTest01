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

def create(request):
    template = loader.get_template('createperson.html')
    return HttpResponse(template.render())

def createAction(request,p1 : Person):
    p1 = Person(
        firstname=p1.firstname,
        lastname=p1.lastname,
        email=p1.email,
        age=p1.age,
        username=p1.username,
        password=p1.password,
    )
    p1.save()
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