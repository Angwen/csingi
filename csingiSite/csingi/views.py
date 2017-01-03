from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import CharacterStory, Players
from .forms import NameForm

# Create your views here.


def index(request):
    return HttpResponse("Ez itten az index")


def player_input(request):
    template = loader.get_template("csingi/player_input.html")
    context = {}
    return HttpResponse(template.render(context, request))

def get_player_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("https://www.youtube.com/watch?v=04854XqcfCY")
        else:
            form = NameForm()
        return render(request, 'player_name.html', {'form': form})


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
