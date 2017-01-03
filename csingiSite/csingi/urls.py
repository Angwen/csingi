from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^karakter/$', views.karakter, name='karakter'),
    url(r'^jatekos/$', views.player, name='player')
]