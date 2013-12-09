from django.contrib import admin
from models import *
from usuarios.models import Usuario
from django.db import connection

# Register your models here.
class TipodocenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ['descripcion']
    search_fields = ['descripcion']

class DocentesAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre','apellidos', 'tipodocente')
 
class JuradosAdmin(admin.ModelAdmin):
    list_display = ('trabajosgrado_codigo','docentes_dni','presidente', 'fecha')
    def save_model(self, request, obj, form, change):
        obj.save()
            
        if not change:
            Usuario.objects.create_userRol(obj.dni, Usuario.JURADO, 'clave123')
            """
            tipo = obj.tipo
            g = Group.objects.get(name=tipo)
            obj.groups.clear()
            obj.groups.add(g)   
            """

class CaracterAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')

class EvaluacionesTrabajoGradoAdmin(admin.ModelAdmin):
    list_display = ('id','fecha','nota_final_aspectos','caracter')

class EstudiantesAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        obj.save()
        
        if not change:
            Usuario.objects.create_userRol(obj.dni, Usuario.ESTUDIANTE, obj.dni)
            """
            est = Estudiantes.objects.create(dni=obj.dni, nombre=obj.nombre, apellidos=obj.apellidos, trabajosgrado_codigo=null )
            tipo = obj.tipo
            g = Group.objects.get(name=tipo)
            obj.groups.clear()
            obj.groups.add(g)   
            """

class CoordinadorestgAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        obj.save()
        d = Docentes.objects.get(pk=obj.docentes_dni)
        if not change:
            Usuario.objects.create_userRol(d.dni, Usuario.COORDINADOR, d.dni)
            
        
        

admin.site.register(Estudiantes, EstudiantesAdmin)
admin.site.register(Tipodocente, TipodocenteAdmin)
admin.site.register(Docentes, DocentesAdmin)
admin.site.register(Caracter, CaracterAdmin)
admin.site.register(Evaluacionestrabajogrado, EvaluacionesTrabajoGradoAdmin)
admin.site.register(Trabajosgrado)
admin.site.register(Jurados, JuradosAdmin)
admin.site.register(Modalidadespasantia)
admin.site.register(Coordinadorestg, CoordinadorestgAdmin)