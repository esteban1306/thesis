# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	#Permite el acceso a la vista de la pagina principal 
    url(r'^$','principal.views.home', name='home'),

    url(r'^estudiante/(\d+)/$', 'principal.views.estudiante_detalle', name='estudiante_detalle'),
    url(r'^estudiante_pdf/(\d+)/$', 'principal.views.estudiante_pdf', name='estudiante_pdf'),
    url(r'^lista_trabajos_pdf/$', 'principal.views.lista_trabajos_pdf', name='lista_trabajos_pdf'),
    url(r'^reporte_criterios_pdf/$', 'principal.views.reporte_criterios_pdf', name='reporte_criterios_pdf'),
    url(r'^trabajo/(\d+)/$', 'principal.views.trabajo_grado_detalle', name='trabajo_grado_detalle'),
    url(r'^trabajos_grado_list$','principal.views.trabajos_grado_list', name='trabajos_grado_list'),
    #Permite el acceso a la vista de la lista de estudiantes
    url(r'^Tipodocente/$','principal.views.lista_estudiantes'),
    #Permite el acceso a la vista de login de usuario
    url(r'^login/$', 'principal.views.login_view', name='vista_login'),
    #Permite el acceso a la vista de logout de usuario
    url(r'^logout/$', 'principal.views.logout_view', name='vista_logout'),
)