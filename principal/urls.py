# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$','principal.views.nuevo_Tipodocente'),
    url(r'^Tipodocente','principal.views.lista_estudiantes'),
)