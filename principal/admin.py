from django.contrib import admin
from models import *

# Register your models here.
class TipodocenteAdmin(admin.ModelAdmin):
	list_display = ('id', 'descripcion')
	list_filter = ['descripcion']
	search_fields = ['descripcion']

class DocentesAdmin(admin.ModelAdmin):
	list_display = ('dni','nombre','apellidos', 'tipodocente')
	
class CaracterAdmin(admin.ModelAdmin):
	list_display = ('id', 'descripcion')

class EvaluacionesTrabajoGradoAdmin(admin.ModelAdmin):
	list_display = ('id','fecha','nota_final_aspectos','caracter')


admin.site.register(Estudiantes)
admin.site.register(Tipodocente, TipodocenteAdmin)
admin.site.register(Docentes, DocentesAdmin)
admin.site.register(Caracter, CaracterAdmin)
admin.site.register(Evaluacionestrabajogrado, EvaluacionesTrabajoGradoAdmin)
admin.site.register(Trabajosgrado)