from django.contrib import admin
from models import *
from usuarios.models import Usuario

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

class EstudiantesAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
       
        obj.save()
        
        if not change:
            Usuario.objects.create_userEstudiante(obj.dni, Usuario.ESTUDIANTE, 'clave123')
            """
            tipo = obj.tipo
            g = Group.objects.get(name=tipo)
            obj.groups.clear()
            obj.groups.add(g)   
            """

admin.site.register(Estudiantes)
admin.site.register(Tipodocente, TipodocenteAdmin)
admin.site.register(Docentes, DocentesAdmin)
admin.site.register(Caracter, CaracterAdmin)
admin.site.register(Evaluacionestrabajogrado, EvaluacionesTrabajoGradoAdmin)
admin.site.register(Trabajosgrado)
admin.site.register(Jurados)
admin.site.register(Modalidadespasantia)