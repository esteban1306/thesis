from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     #url(r'^$', 'thesis.views.home', name='home'),
     #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','principal.views.nuevo_Tipodocente'),
    url(r'^Tipodocente','principal.views.lista_estudiantes'),
)