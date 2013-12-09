from django.contrib import admin
#Importar todo desde models
from models import *
from usuarios.models import Usuario

#Define un modelo de administracion para Tipodocente
class TipodocenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ['descripcion']
    search_fields = ['descripcion']

#Define un modelo de administracion para Docentes
class DocentesAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre','apellidos', 'tipodocente')

#Define un modelo de administracion para Jurados
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

#Define un modelo de administracion para Caracter
class CaracterAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')

#Define un modelo de administracion para EvaluacionesTrabajogrado
class EvaluacionesTrabajoGradoAdmin(admin.ModelAdmin):
    list_display = ('id','fecha','nota_final_aspectos','caracter')

#Define un modelo de administracion para Estudiantes
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

<<<<<<< HEAD
# Registro de los modelos

#Agregar el modelo Estudiantes dentro de la interfaz administrativa
=======
class CoordinadorestgAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        obj.save()
        d = Docentes.objects.get(pk=obj.docentes_dni)
        if not change:
            Usuario.objects.create_userRol(d.dni, Usuario.COORDINADOR, d.dni)
            
        
>>>>>>> 547c2c341e3754d0652c24a20e2a27b38d700790
admin.site.register(Estudiantes, EstudiantesAdmin)
#Agregar el modelo Tipodocente dentro de la interfaz administrativa
admin.site.register(Tipodocente, TipodocenteAdmin)
#Agregar el modelo Docentes dentro de la interfaz administrativa
admin.site.register(Docentes, DocentesAdmin)
#Agregar el modelo Caracter dentro de la interfaz administrativa
admin.site.register(Caracter, CaracterAdmin)
#Agregar el modelo Evaluacionestrabajogrado dentro de la interfaz administrativa
admin.site.register(Evaluacionestrabajogrado, EvaluacionesTrabajoGradoAdmin)
#Agregar el modelo Trabajosgrado dentro de la interfaz administrativa
admin.site.register(Trabajosgrado)
#Agregar el modelo Jurados dentro de la interfaz administrativa
admin.site.register(Jurados, JuradosAdmin)
<<<<<<< HEAD
#Agregar el modelo Modalidadespasantia dentro de la interfaz administrativa
admin.site.register(Modalidadespasantia)
=======
admin.site.register(Modalidadespasantia)
admin.site.register(Concejocurricular)
admin.site.register(Asesores)
admin.site.register(Aspectos)
admin.site.register(Conceptossolicitudes)
admin.site.register(Conveniomarco)
admin.site.register(Convocatorias)
admin.site.register(Coordinadorestg)
admin.site.register(Criterios)
admin.site.register(Criteriosaspectos)
admin.site.register(Criteriosjurado)
admin.site.register(Cronogramas)
admin.site.register(DocentesConsejocurricular)
admin.site.register(Documentacion)
admin.site.register(Empresaspasantes)
admin.site.register(Historicocriteriospropuestas)
admin.site.register(InformefinalCriterios)
admin.site.register(Informesfinales)
admin.site.register(Informesperiodicos)
admin.site.register(Modalidadestg)
admin.site.register(Pasantias)
admin.site.register(Propuestatg)
admin.site.register(PropuestatgRevisorest)
admin.site.register(Revisorestecnicos)
admin.site.register(Solicitudespasantes)
admin.site.register(Supervisoresempresas)
admin.site.register(Sustentaciones)
admin.site.register(Tiposempresa)
admin.site.register(Visitas)
>>>>>>> 547c2c341e3754d0652c24a20e2a27b38d700790
