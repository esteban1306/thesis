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
    list_filter = ['nombre']
    search_fields = ['nombre']

#Define un modelo de administracion para Asesores
class AsesoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'trabajosgrado_codigo','docentes_dni', 'fecha')
    readonly_fields = ('id',)
    search_fields = ('id',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id = Asesores.objects.all().count() + 1
            obj.save()
        obj.save()
    

#Define un modelo de administracion para Jurados

class JuradosAdmin(admin.ModelAdmin):
    list_display = ('trabajosgrado_codigo','docentes_dni','presidente', 'fecha')
    def save_model(self, request, obj, form, change):
        obj.save()
        d = Docentes.objects.filter(pk=obj.docentes_dni)
        if not change:
            Usuario.objects.create_userRol(d.dni, Usuario.JURADO, d.dni)
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
    list_display = ('dni','nombre','apellidos')
    list_filter = ['apellidos']
    search_fields = ['nombre'] 
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

class VisitasAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'hora' )
    list_filter = ['id']
    search_fields = ['id']

class trabajosgradoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo', 'grupo_investigacion', 'nota_definitiva' )
    list_filter = ['codigo']
    search_fields = ['titulo']    

class TiposempresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ['descripcion']
    search_fields = ['descripcion']


class SustentacionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'fechapublicacion', 'fecharealizacion', 'hora','lugar' , 'nota')
    list_filter = ['id']
    search_fields = ['id']  

class SupervisoresempresasAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellidos', 'cargo')
    list_filter = ['nombre']
    search_fields = ['nombre']      

class SolicitudespasantesAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'link')
    list_filter = ['id']
    search_fields = ['id']      
class RevisorestecnicosAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ['id']
    search_fields = ['id']  

class PropuestatgAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fechapresentacion', 'link')
    list_filter = ['id']
    search_fields = ['id']    

class PasantiasAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'propuestaspasantias_id')
    list_filter = ['codigo']
    search_fields = ['codigo'] 

class ModalidadestgAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ['id']
    search_fields = ['id'] 

class ModalidadespasantiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ['id']
    search_fields = ['id'] 

class InformesperiodicosAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'fecha')
    list_filter = ['id']
    search_fields = ['id'] 

class InformesfinalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'link')
    list_filter = ['id']
    search_fields = ['id'] 

class InformefinalCriteriosAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'link')
    list_filter = ['fecha']
    search_fields = ['fecha'] 

class HistoricocriteriospropuestasAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'link')
    list_filter = ['fecha']
    search_fields = ['link']                                  
# Registro de los modelos

#Agregar el modelo Estudiantes dentro de la interfaz administrativa
class CoordinadorestgAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        obj.save()
        d = Docentes.objects.get(pk=obj.docentes_dni)
        if not change:
            Usuario.objects.create_userRol(d.dni, Usuario.COORDINADOR, d.dni)
            
        
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
admin.site.register(Trabajosgrado, trabajosgradoAdmin)
#Agregar el modelo Jurados dentro de la interfaz administrativa
admin.site.register(Jurados, JuradosAdmin)
#Agregar el modelo Modalidadespasantia dentro de la interfaz administrativa
admin.site.register(Modalidadespasantia)
#Agregar el modelo Modalidadespasantia dentro de la interfaz administrativa
admin.site.register(Concejocurricular)
admin.site.register(Asesores, AsesoresAdmin)
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
admin.site.register(Historicocriteriospropuestas,HistoricocriteriospropuestasAdmin)
admin.site.register(InformefinalCriterios,InformefinalCriteriosAdmin)
admin.site.register(Informesfinales,InformesfinalesAdmin)
admin.site.register(Informesperiodicos,InformesperiodicosAdmin)
admin.site.register(Modalidadestg, ModalidadestgAdmin)
admin.site.register(Pasantias, PasantiasAdmin)
admin.site.register(Propuestatg, PropuestatgAdmin)
admin.site.register(Revisorestecnicos, RevisorestecnicosAdmin)
admin.site.register(Solicitudespasantes, SolicitudespasantesAdmin)
admin.site.register(Supervisoresempresas, SupervisoresempresasAdmin)
admin.site.register(Sustentaciones,SustentacionesAdmin)
admin.site.register(Tiposempresa,TiposempresaAdmin)
admin.site.register(Visitas, VisitasAdmin)