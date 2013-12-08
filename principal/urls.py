# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$','principal.views.home'),
    url(r'^Tipodocente/$','principal.views.lista_estudiantes'),
    url(r'^login/$', 'principal.views.login_view', name='vista_login'),
    url(r'^logout/$', 'principal.views.logout_view', name='vista_logout'),
)