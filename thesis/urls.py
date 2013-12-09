from django.conf.urls import patterns, include, url
import settings

#Habilitar la aplicacion de administracion
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     #url(r'^$', 'thesis.views.home', name='home'),
     #url(r'^blog/', include('blog.urls')),

    #Habilitar direccion del administrador
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^', include('principal.urls')),
   	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)