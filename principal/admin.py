from django.contrib import admin
#Importar todo desde models
from models import *
from usuarios.models import Usuario
from django.contrib.auth.models import Group
from django.db.models import Max

#-------Modelos de Administracion para los Roles-------------------#

#Define un modelo de administracion para Estudiantes
class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre','apellidos')
    list_filter = ['apellidos']
    search_fields = ['nombre']

    def save_model(self, request, obj, form, change):
        if change:
            obj.save()
        else:
            #nombre = obj.__class__.__name__
            obj.save()
            user = Usuario.objects.create_userRol(obj.dni, Usuario.ESTUDIANTE, obj.dni)
            
            grupo = Group.objects.get(name=Usuario.ESTUDIANTE)
            user.groups.add(grupo)

#Define un modelo de administracion para Docentes
class DocentesAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre','apellidos', 'tipodocente')
    list_filter = ['nombre']
    search_fields = ['nombre']

#Agregar el modelo Estudiantes dentro de la interfaz administrativa
class CoordinadorestgAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.save()
        else:
            obj.save()
            dni = obj.docentes_dni.dni
            user = Usuario.objects.create_userRol(dni, Usuario.COORDINADOR, dni)

            grupo = Group.objects.get(name='coordinador')
            user.groups.add(grupo)

#Define un modelo de administracion para Asesores
class AsesoresAdmin(admin.ModelAdmin):

    list_display = ('id','trabajosgrado_codigo','docentes_dni', 'fecha')

    
    def add_view(self, *args, **kwargs):
        self.fields = ('trabajosgrado_codigo','docentes_dni','fecha')
        return super(AsesoresAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if change:
            obj.save()
        else:
            #nombre = obj.__class__.__name__            
            obj.id = Asesores.objects.all().count() + 1
            obj.save()
            dni = obj.docentes_dni.dni
            user = Usuario.objects.create_userRol(dni, Usuario.ASESOR, dni)
            
            grupo = Group.objects.get(name='asesor')
            user.groups.add(grupo)

#Define un modelo de administracion para Jurados

class JuradosAdmin(admin.ModelAdmin):
    list_display = ('trabajosgrado_codigo','docentes_dni','presidente', 'fecha')

    def save_model(self, request, obj, form, change):
        if change:
            obj.save()
        else:
            obj.save()
            dni = obj.docentes_dni.dni
            user = Usuario.objects.create_userRol(dni, Usuario.JURADO, dni)
            
            grupo = Group.objects.get(name='jurado')
            user.groups.add(grupo)   

"""
    Modelos de Administracion para el resto de entidades
"""
#Define un modelo de administracion para Aspectos
class AspectosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'porcentaje')
    search_fields = ['descripcion']

#Define un modelo de administracion para Caracter
class CaracterAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ['descripcion']

#Define un modelo de administracion para Concejo curricular
class ConcejocurricularAdmin(admin.ModelAdmin):
    list_display = ('id', 'fechacreacion')
    search_fields = ['fechacreacion']

#Define un modelo de administracion para Conceptos solicitudes
class ConceptossolicitudesAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ['descripcion']

#Define un modelo de administracion para Conveniosmarco
class ConveniosmarcoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'activo', 'empresaspasantes_nit')
    search_fields = ['empresaspasantes_nit', 'fecha']

#Define un modelo de administracion para Convocatorias
class ConvocatoriasAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'fechainicio', 'fechalimite')
    search_fields = ['descripcion']

#Define un modelo de administracion para Criterios
class CriteriosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ['descripcion']

#Define un modelo de administracion para CriteriosAspectos
class CriteriosaspectosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'porcentaje', 'calificacion')
    search_fields = ['descripcion']

#Define un modelo de administracion para Criteriosjurados
class CriteriosjuradosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ['descripcion']

#Define un modelo de administracion para Cronogramas
class CronogramasAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'fechainicio', 'fechafin', 'trabajosgrado_codigo')
    search_fields = ['descripcion']

#Define un modelo de administracion para Docentesconcejorcurricular
class DocentesconcejocurricularAdmin(admin.ModelAdmin):
    list_display = ('concejocurricular', 'docentes_dni')
    list_filter = ['docentes_dni']
    search_fields = ['docentes_dni']

#Define un modelo de administracion para DocumentacionAdmin
class DocumentacionAdmin(admin.ModelAdmin):
    list_display =('id', 'fecha', 'asunto', 'descripcion', 'trabajosgrado_codigo', 'link')
    search_fields = ['asunto']

#Define un modelo de administracion para Empreaspasantes
class EmpresaspasantesAdmin(admin.ModelAdmin):
    list_display = ('nit', 'nombre', 'direccion', 'tiposempresa')
    search_fields = ['nombre']
    list_filter = ['nombre']

#Define un modelo de administracion para EvaluacionesTrabajogrado
class EvaluacionesTrabajoGradoAdmin(admin.ModelAdmin):
    list_display = ('id','fecha','nota_final_aspectos','caracter')
    search_fields = ['caracter']

#Define un modelo de administracion para Historicocriteriospropuestas
class HistoricocriteriospropuestasAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'link')
    list_filter = ['fecha']
    search_fields = ['link']

#Define un modelo de administracion para Informesfinales
class InformesfinalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'link')
    list_filter = ['id']
    search_fields = ['id']

#Define un modelo de administracion para Informefinalcriterios
class InformefinalCriteriosAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'link')
    list_filter = ['fecha']
    search_fields = ['fecha']

#Define un modelo de administracion para Informesperiodicos
class InformesperiodicosAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'fecha')
    list_filter = ['id']
    search_fields = ['id']

#Define un modelo de administracion para Modalidadespasantia
class ModalidadespasantiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ['id']
    search_fields = ['id']

#Define un modelo de administracion para Modalidades de trabajo de grado
class ModalidadestgAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ['id']
    search_fields = ['id'] 

#Define un modelo de administracion para Pasantias
class PasantiasAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'propuestaspasantias_id')
    list_filter = ['codigo']
    search_fields = ['codigo']

#Define un modelo de administracion para Propuestas de trabajo de grado
class PropuestatgAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fechapresentacion', 'link')
    list_filter = ['id']
    search_fields = ['id']

#Define un modelo de administracion para Propuestas de trabajo de grado
class PropuestatgRevisorestAdmin(admin.ModelAdmin):
    list_display = ('id', 'propuestatg', 'revisorestecnicos')
    list_filter = ['id']
    search_fields = ['id']

#Define un modelo de administracion para Revisores Tecnicos
class RevisorestecnicosAdmin(admin.ModelAdmin):
    list_display = ('id', 'concepto', 'docentes_dni')
    list_filter = ['id']
    search_fields = ['id']

#Define un modelo de administracion para Solicitudes pasantes
class SolicitudespasantesAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'empresaspasantes', 'concejocurricular', 'conceptossolicitudes', 'link', 'revisorestecnicos')
    list_filter = ['id']
    search_fields = ['id']

#Define un modelo de administracion para Supervisores empresas
class SupervisoresempresasAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellidos', 'cargo', 'empresaspasantes_nit')
    list_filter = ['nombre']
    search_fields = ['nombre']

#Define un modelo de administracion para Sustentaciones
class SustentacionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'fechapublicacion', 'fecharealizacion', 'hora','lugar' , 'nota', 'trabajosgrado_codigo')
    list_filter = ['id']
    search_fields = ['id']

#Define un modelo de administracion para Tipodocente
class TipodocenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ['descripcion']
    search_fields = ['descripcion']

    def add_view(self, *args, **kwargs):
        self.fields = ('descripcion',)
        return super(TipodocenteAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if change:
            obj.save()
        else:
            #nombre = obj.__class__.__name__
            maximo = Tipodocente.objects.all().aggregate(m=Max('id'))
            print maximo
            obj.id  = maximo['m'] + 1
            obj.save()

#Define un modelo de administracion para Tiposempresa
class TiposempresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ['descripcion']
    search_fields = ['descripcion']    

#Define un modelo de administracion para Trabajosgrado
class TrabajosgradoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo', 'grupo_investigacion', 'nota_definitiva', 'docentes_director' )
    list_filter = ['codigo']


#Define un modelo de administracion para Visistas
class VisitasAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'hora', 'coordinadorestg', 'empresaspasantes_nit' )
    list_filter = ['id']
    search_fields = ['id']

"""
    Registro de los modelos en el panel administrativo
"""     
#Agregar el modelo Asesores dentro de la interfaz administrativa
admin.site.register(Asesores, AsesoresAdmin)
#Agregar el modelo Aspectos dentro de la interfaz administrativa
admin.site.register(Aspectos, AspectosAdmin)
#Agregar el modelo Caracter dentro de la interfaz administrativa
admin.site.register(Caracter, CaracterAdmin)
#Agregar el modelo Concejocurricular dentro de la interfaz administrativa
admin.site.register(Concejocurricular, ConcejocurricularAdmin)
#Agregar el modelo Conceptossolicitudes dentro de la interfaz administrativa
admin.site.register(Conceptossolicitudes, ConceptossolicitudesAdmin)
#Agregar el modelo Conveniosmarco dentro de la interfaz administrativa
admin.site.register(Conveniomarco, ConveniosmarcoAdmin)
#Agregar el modelo Convocatorias dentro de la interfaz administrativa
admin.site.register(Convocatorias, ConvocatoriasAdmin)
#Agregar el modelo Coordinadorestg dentro de la interfaz administrativa
admin.site.register(Coordinadorestg, CoordinadorestgAdmin)
#Agregar el modelo Criterios dentro de la interfaz administrativa
admin.site.register(Criterios, CriteriosAdmin)
#Agregar el modelo Criteriosaspectos dentro de la interfaz administrativa
admin.site.register(Criteriosaspectos, CriteriosaspectosAdmin)
#Agregar el modelo Criteriosjurados dentro de la interfaz administrativa
admin.site.register(Criteriosjurado, CriteriosjuradosAdmin)
#Agregar el modelo Cronogramas dentro de la interfaz administrativa
admin.site.register(Cronogramas, CronogramasAdmin)
#Agregar el modelo Docentes dentro de la interfaz administrativa
admin.site.register(Docentes, DocentesAdmin)
#Agregar el modelo Docentesconcejocurricular dentro de la interfaz administrativa
admin.site.register(DocentesConsejocurricular, DocentesconcejocurricularAdmin)
#Agregar el modelo Documentacion dentro de la interfaz administrativa
admin.site.register(Documentacion, DocumentacionAdmin)
#Agregar el modelo Empresaspasantes dentro de la interfaz administrativa
admin.site.register(Empresaspasantes, EmpresaspasantesAdmin)
#Agregar el modelo Estudiantes dentro de la interfaz administrativa
admin.site.register(Estudiantes, EstudiantesAdmin)
#Agregar el modelo Evaluacionestrabajogrado dentro de la interfaz administrativa
admin.site.register(Evaluacionestrabajogrado, EvaluacionesTrabajoGradoAdmin)

#Agregar el modelo Historicocriteriospropuestas dentro de la interfaz administrativa

admin.site.register(Historicocriteriospropuestas,HistoricocriteriospropuestasAdmin)
#Agregar el modelo Informesfinales dentro de la interfaz administrativa
admin.site.register(Informesfinales,InformesfinalesAdmin)
#Agregar el modelo Informefinalcriterios dentro de la interfaz administrativa
admin.site.register(InformefinalCriterios,InformefinalCriteriosAdmin)
#Agregar el modelo Informesperiodicos dentro de la interfaz administrativa
admin.site.register(Informesperiodicos,InformesperiodicosAdmin)
#Agregar el modelo Jurados dentro de la interfaz administrativa
admin.site.register(Jurados, JuradosAdmin)
#Agregar el modelo Modalidadespasantia dentro de la interfaz administrativa
admin.site.register(Modalidadespasantia, ModalidadespasantiaAdmin)
#Agregar el modelo Modalidadestg dentro de la interfaz administrativa
admin.site.register(Modalidadestg, ModalidadestgAdmin)
#Agregar el modelo Pasantias dentro de la interfaz administrativa
admin.site.register(Pasantias, PasantiasAdmin)
#Agregar el modelo Propuestastg dentro de la interfaz administrativa
admin.site.register(Propuestatg, PropuestatgAdmin)
#Agregar el modelo RevisoresTecnicos dentro de la interfaz administrativa
admin.site.register(Revisorestecnicos, RevisorestecnicosAdmin)
#Agregar el modelo Propuestas_Trabajos de Grado_Revisores Tecnicos dentro de la interfaz administrativa
admin.site.register(PropuestatgRevisorest, PropuestatgRevisorestAdmin)
#Agregar el modelo Solicitudespasantes dentro de la interfaz administrativa
admin.site.register(Solicitudespasantes, SolicitudespasantesAdmin)
#Agregar el modelo Supervisoresempresas dentro de la interfaz administrativa
admin.site.register(Supervisoresempresas, SupervisoresempresasAdmin)
#Agregar el modelo Sustentaciones dentro de la interfaz administrativa
admin.site.register(Sustentaciones,SustentacionesAdmin)
#Agregar el modelo Tipodocente dentro de la interfaz administrativa
admin.site.register(Tipodocente, TipodocenteAdmin)
#Agregar el modelo Tiposempresa dentro de la interfaz administrativa
admin.site.register(Tiposempresa,TiposempresaAdmin)
#Agregar el modelo Trabajosgrado dentro de la interfaz administrativa
admin.site.register(Trabajosgrado, TrabajosgradoAdmin)
#Agregar el modelo Vistas dentro de la interfaz administrativa
admin.site.register(Visitas, VisitasAdmin)