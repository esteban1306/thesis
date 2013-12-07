from django.contrib import admin
from models import Estudiantes, Tipodocente

# Register your models here.
class TipodocenteAdmin(admin.ModelAdmin):
	list_display = ('id', 'descripcion')
	list_filter = ['descripcion']
	search_fields = ['descripcion']

admin.site.register(Estudiantes)
admin.site.register(Tipodocente, TipodocenteAdmin)