from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import CharacterStory, Players

# Create your views here.


def index():
    pass

def player(request):
    data = Players.objects.all()
    template = loader.get_template("csingi/player.html")
    context = {
        "data": data
    }
    return HttpResponse(template.render(context, request))


def karakter(request):
    data = CharacterStory.objects.all()
    kiskutya = "tiiriitititi"
    template = loader.get_template("csingi/karakter.html")
    context = {
        "data": data,
        "kiskutya": kiskutya
    }
    return HttpResponse(template.render(context, request))
