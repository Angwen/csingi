from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jatekos_regisztralas/$', views.player_input, name='player_input'),
    url(r'^your-name/$', views.get_player_name, name='your-name'),
    url(r'^karakter/$', views.karakter, name='karakter'),
    url(r'^jatekos/$', views.player, name='player')
]