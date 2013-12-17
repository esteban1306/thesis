# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	#Permite el acceso a la vista de la pagina principal 
    url(r'^$','principal.views.home'),

    url(r'^trabajos_grado_list$','principal.views.trabajos_grado_list', name='trabajos_grado_list'),
    #Permite el acceso a la vista de la lista de estudiantes
    url(r'^Tipodocente/$','principal.views.lista_estudiantes'),
    #Permite el acceso a la vista de login de usuario
    url(r'^login/$', 'principal.views.login_view', name='vista_login'),
    #Permite el acceso a la vista de logout de usuario
    url(r'^logout/$', 'principal.views.logout_view', name='vista_logout'),
)