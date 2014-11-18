# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView
from encuestas.models import Pregunta, Noticia
from django.conf.urls import patterns, url

from encuestas import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^noticias/$', ListView.as_view(model=Noticia), name='noticias'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Pregunta,),
        name='detalle'),


    url(r'^(?P<pk>\d+)/resultados/$', views.ResultadosView.as_view(), 
        name='resultados'),
    url(r'^(?P<pregunta_id>\d+)/votar/$', views.votar, name='votar'),
)

