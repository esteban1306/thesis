# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	#Permite el acceso a la vista de la pagina principal 
    url(r'^$','principal.views.home', name='home'),

    url(r'^estudiante/(\d+)/$', 'principal.views.estudiante_detalle', name='estudiante_detalle'),

    url(r'^asesor/(\d+)/$', 'principal.views.asesor_detalle', name='asesor_detalle'),
    url(r'^coordinador/(\d+)/$', 'principal.views.coordinador_detalle', name='coordinador_detalle'),
    url(r'^jurado/(\d+)/$', 'principal.views.jurado_detalle', name='jurado_detalle'),
    url(r'^director/(\d+)/$', 'principal.views.director_detalle', name='director_detalle'),

    url(r'^trabajos/asesor/(\d+)/$','principal.views.trabajos_grado_list_asesor', name='trabajos_grado_list_asesor'),
    url(r'^trabajos/coordinador/(\d+)/$','principal.views.trabajos_grado_list_coordinador', name='trabajos_grado_list_coordinador'),
    url(r'^trabajos/jurado/(\d+)/$','principal.views.trabajos_grado_list_jurado', name='trabajos_grado_list_jurado'),
    url(r'^trabajos/director/(\d+)/$','principal.views.trabajos_grado_list_director', name='trabajos_grado_list_director'),


    url(r'^trabajo/(\d+)/$', 'principal.views.trabajo_grado_detalle', name='trabajo_grado_detalle'),

    url(r'^trabajos_grado_list$','principal.views.trabajos_grado_list_asesor', name='trabajos_grado_list'),
    #Permite el acceso a la vista de la lista de estudiantes
    url(r'^Tipodocente/$','principal.views.lista_estudiantes'),
    #Permite el acceso a la vista de login de usuario
    url(r'^login/$', 'principal.views.login_view', name='vista_login'),
    #Permite el acceso a la vista de logout de usuario
    url(r'^logout/$', 'principal.views.logout_view', name='vista_logout'),
)