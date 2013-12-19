# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
#Importar todo desde models
from models import *
from usuarios.models import Usuario
from django.db.models import Max

#-------Modelos de Administracion para los Roles-------------------#

#Define un modelo de administracion para Estudiantes
class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre','apellidos')
    list_filter = ['apellidos']
    search_fields = ['nombre']

    def save_model(self, request, obj, form, change):
        obj.save()
        if not change:
            user = Usuario.objects.create_userRol(obj.dni, Usuario.ESTUDIANTE, obj.dni)
            

#Define un modelo de administracion para Docentes
class DocentesAdmin(admin.ModelAdmin):
    list_display  = ('dni','nombre','apellidos', 'tipodocente')
    list_filter   = ['nombre']
    search_fields = ['nombre']
    """
    def save_model(self, request, obj, form, change):
        obj.save()
        if not change:
            Usuario.objects.create_userRol(obj.dni, obj.tipodocente.descripcion, obj.dni)
    """   
            

#Agregar el modelo Estudiantes dentro de la interfaz administrativa
class CoordinadorestgAdmin(admin.ModelAdmin):
    
    list_display = ('id','docentes_dni','anio', 'semestreacademico')
    
    def add_view(self, *args, **kwargs):
        self.fields = ('docentes_dni','anio','semestreacademico')
        return super(CoordinadorestgAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
            dni = obj.docentes_dni.dni
            user = Usuario.objects.create_userRol(dni, Usuario.COORDINADOR, dni)
        obj.save()          
         

#Define un modelo de administracion para Asesores
class AsesoresAdmin(admin.ModelAdmin):

    list_display = ('id','trabajosgrado_codigo','docentes_dni', 'fecha')
    
    def add_view(self, *args, **kwargs):
        self.fields = ('trabajosgrado_codigo','docentes_dni','fecha')
        return super(AsesoresAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
            dni = obj.docentes_dni.dni
            user = Usuario.objects.create_userRol(dni, Usuario.ASESOR, dni)
        obj.save() 

#Define un modelo de administracion para Jurados
class JuradosAdmin(admin.ModelAdmin):
    list_display = ('id', 'trabajosgrado_codigo','docentes_dni', 'concejocurricular', 'presidente', 'fecha')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
            dni = obj.docentes_dni.dni
            user = Usuario.objects.create_userRol(dni, Usuario.JURADO, dni)
        obj.save()   

    def add_view(self, *args, **kwargs):
        self.fields = ('trabajosgrado_codigo','docentes_dni', 'concejocurricular', 'presidente', 'fecha')
        return super(JuradosAdmin, self).add_view(*args, **kwargs)


"""
    Modelos de Administracion para el resto de entidades
"""
#Define un modelo de administracion para Aspectos
class AspectosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'porcentaje')
    search_fields = ['descripcion']

    def add_view(self, *args, **kwargs):
        self.fields = ('descripcion', 'porcentaje', 'evaluacionestrabajogrado')
        return super(AspectosAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()  

#Define un modelo de administracion para Caracter
class CaracterAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ['descripcion']

    def add_view(self, *args, **kwargs):
        self.fields = ('descripcion',)
        return super(CaracterAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()        

#Define un modelo de administracion para Concejo curricular
class ConcejocurricularAdmin(admin.ModelAdmin):
    list_display = ('id', 'fechacreacion')
    search_fields = ['fechacreacion']

    def add_view(self, *args, **kwargs):
        self.fields = ('fechacreacion',)
        return super(ConcejocurricularAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()    

#Define un modelo de administracion para Conceptos solicitudes
class ConceptossolicitudesAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ['descripcion']

    def add_view(self, *args, **kwargs):
        self.fields = ('descripcion',)
        return super(ConceptossolicitudesAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save() 

#Define un modelo de administracion para Conveniosmarco
class ConveniosmarcoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'activo', 'empresaspasantes_nit')
    search_fields = ['empresaspasantes_nit', 'fecha']

    def add_view(self, *args, **kwargs):
        self.fields = ('fecha', 'activo', 'empresaspasantes_nit')
        return super(ConveniosmarcoAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

#Define un modelo de administracion para Convocatorias
class ConvocatoriasAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'fechainicio', 'fechalimite')
    search_fields = ['descripcion']

    def add_view(self, *args, **kwargs):
        self.fields = ('descripcion', 'fechainicio', 'fechalimite', 'solicitudespasantes')
        return super(ConvocatoriasAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

#Define un modelo de administracion para Criterios
class CriteriosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ['descripcion']

    def add_view(self, *args, **kwargs):
        self.fields = ('descripcion', )
        return super(CriteriosAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

#Define un modelo de administracion para CriteriosAspectos
class CriteriosaspectosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'porcentaje', 'calificacion')
    search_fields = ['descripcion']

    def add_view(self, *args, **kwargs):
        self.fields = ('descripcion', 'porcentaje', 'calificacion', 'aspectos',)
        return super(CriteriosaspectosAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

#Define un modelo de administracion para Criteriosjurados
class CriteriosjuradosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ['descripcion']

    def add_view(self, *args, **kwargs):
        self.fields = ('descripcion',)
        return super(CriteriosjuradosAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

#Define un modelo de administracion para Cronogramas
class CronogramasAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'fechainicio', 'fechafin', 'trabajosgrado_codigo')
    search_fields = ['descripcion']

    def add_view(self, *args, **kwargs):
        self.fields = ('descripcion', 'fechainicio', 'fechafin', 'trabajosgrado_codigo')
        return super(CronogramasAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

#Define un modelo de administracion para Docentesconcejorcurricular
class DocentesconcejocurricularAdmin(admin.ModelAdmin):
    list_display = ('id', 'concejocurricular', 'docentes_dni')
    list_filter = ['docentes_dni']
    search_fields = ['docentes_dni']

    def add_view(self, *args, **kwargs):
        self.fields = ('concejocurricular', 'docentes_dni')
        return super(DocentesconcejocurricularAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

#Define un modelo de administracion para DocumentacionAdmin
class DocumentacionAdmin(admin.ModelAdmin):
    list_display =('id', 'fecha', 'asunto', 'descripcion', 'trabajosgrado_codigo', 'link')
    search_fields = ['asunto']

    def add_view(self, *args, **kwargs):
        self.fields = ('fecha', 'asunto', 'descripcion', 'trabajosgrado_codigo', 'link', 'documentacion')
        return super(DocumentacionAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

    def queryset(self, request):
        qs = super(DocumentacionAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.tipo == Usuario.JURADO:
            jurado_filtrado = Jurados.objects.filter(docentes_dni=request.user.dni).values('trabajosgrado_codigo')
            trabajos_jurados = Trabajosgrado.objects.filter(codigo__in=jurado_filtrado)

            return qs.filter(trabajosgrado_codigo=trabajos_jurados)
        return qs
        if request.user.tipo == Usuario.ASESOR:
            asesor_filtrado = Asesores.objects.filter(docentes_dni=request.user.dni).values('trabajosgrado_codigo')
            trabajos_asesores = Trabajosgrado.objects.filter(codigo__in=asesor_filtrado)

            return qs.filter(trabajosgrado_codigo=trabajos_asesores)
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "trabajosgrado_codigo":
            if request.user.tipo == Usuario.JURADO:
                jurado_filtrado = Jurados.objects.filter(docentes_dni=request.user.dni).values('trabajosgrado_codigo')
                trabajos_jurados = Trabajosgrado.objects.filter(codigo__in=jurado_filtrado)
                kwargs["queryset"] = Trabajosgrado.objects.filter(codigo__in=trabajos_jurados)
        return super(DocumentacionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

#Define un modelo de administracion para Empreaspasantes
class EmpresaspasantesAdmin(admin.ModelAdmin):
    list_display = ('nit', 'nombre', 'direccion', 'tiposempresa')
    search_fields = ['nombre']
    list_filter = ['nombre']

#Define un modelo de administracion para EvaluacionesTrabajogrado
class EvaluacionesTrabajoGradoAdmin(admin.ModelAdmin):
    list_display = ('id','fecha','nota_final_aspectos','caracter')
    search_fields = ['caracter']

    def add_view(self, *args, **kwargs):
        self.fields = ('fecha','nota_final_aspectos','caracter', 'trabajosgrado_codigo')
        return super(EvaluacionesTrabajoGradoAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

    def queryset(self, request):
        qs = super(EvaluacionesTrabajoGradoAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.tipo == Usuario.JURADO:
            jurado_filtrado = Jurados.objects.filter(docentes_dni=request.user.dni).values('trabajosgrado_codigo')
            trabajos_jurados = Trabajosgrado.objects.filter(codigo__in=jurado_filtrado)

            return qs.filter(trabajosgrado_codigo__in=trabajos_jurados)
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "trabajosgrado_codigo":
            if request.user.tipo == Usuario.JURADO:
                jurado_filtrado = Jurados.objects.filter(docentes_dni=request.user.dni).values('trabajosgrado_codigo')
                trabajos_jurados = Trabajosgrado.objects.filter(codigo__in=jurado_filtrado)
                kwargs["queryset"] = Trabajosgrado.objects.filter(codigo__in=trabajos_jurados)
        return super(EvaluacionesTrabajoGradoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

#Define un modelo de administracion para Historicocriteriospropuestas
class HistoricocriteriospropuestasAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'link')
    list_filter = ['fecha']
    search_fields = ['link']

    def add_view(self, *args, **kwargs):
        self.fields = ('fecha', 'criterios', 'concejocurricular', 'propuestatg_revisorest', 'link')
        return super(HistoricocriteriospropuestasAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

#Define un modelo de administracion para Informesfinales
class InformesfinalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'link')
    list_filter = ['id']
    search_fields = ['id']

    def add_view(self, *args, **kwargs):
        self.fields = ('titulo', 'fecha', 'concejocurricular', 'coordinadorestg', 'trabajosgrado_codigo', 'link')
        return super(InformesfinalesAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

    def queryset(self, request):
        qs = super(InformesfinalesAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.tipo == Usuario.JURADO:
            jurado_filtrado = Jurados.objects.filter(docentes_dni=request.user.dni).values('trabajosgrado_codigo')
            trabajos_jurados = Trabajosgrado.objects.filter(codigo__in=jurado_filtrado)

            return qs.filter(trabajosgrado_codigo__in=trabajos_jurados)
        return qs

#Define un modelo de administracion para Informefinalcriterios
class InformefinalCriteriosAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'link')
    list_filter = ['fecha']
    search_fields = ['fecha']

    def add_view(self, *args, **kwargs):
        self.fields = ('fecha', 'informesfinales', 'criteriosjurado', 'jurados','link')
        return super(InformefinalCriteriosAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "jurados":
            kwargs["queryset"] = Jurados.objects.filter(docentes_dni=request.user.dni)
        return super(InformefinalCriteriosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

#Define un modelo de administracion para Informesperiodicos
class InformesperiodicosAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'link')
    list_filter = ['id']
    search_fields = ['id']

    def add_view(self, *args, **kwargs):
        self.fields = ('fecha', 'link', 'pasantias_trabajosgrado_codigo')
        return super(InformesperiodicosAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

#Define un modelo de administracion para Modalidadespasantia
class ModalidadespasantiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ['id']
    search_fields = ['id']

    def add_view(self, *args, **kwargs):
        self.fields = ('descripcion',)
        return super(ModalidadespasantiaAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

#Define un modelo de administracion para Modalidades de trabajo de grado
class ModalidadestgAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ['id']
    search_fields = ['id'] 

    def add_view(self, *args, **kwargs):
        self.fields = ('descripcion',)
        return super(ModalidadestgAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

#Define un modelo de administracion para Pasantias
class PasantiasAdmin(admin.ModelAdmin):
    list_display = ('trabajosgrado_codigo', 'empresaspasantes', 'modalidadespasantia')
    list_filter = ['trabajosgrado_codigo']
    search_fields = ['trabajosgrado_codigo']

#Define un modelo de administracion para Propuestas de trabajo de grado
class PropuestatgAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fechapresentacion', 'link')
    list_filter = ['id']
    search_fields = ['id']

    def add_view(self, *args, **kwargs):
        self.fields = ('titulo', 'fechapresentacion', 'coordinadorestg', 'trabajosgrado_codigo', 'link')
        return super(PropuestatgAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

    def queryset(self, request):
        qs = super(PropuestatgAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.tipo == Usuario.JURADO:
            jurado_filtrado = Jurados.objects.filter(docentes_dni=request.user.dni).values('trabajosgrado_codigo')
            trabajos_jurados = Trabajosgrado.objects.filter(codigo__in=jurado_filtrado)

            return qs.filter(trabajosgrado_codigo=trabajos_jurados)
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "trabajosgrado_codigo":
            if request.user.tipo == Usuario.JURADO:
                jurado_filtrado = Jurados.objects.filter(docentes_dni=request.user.dni).values('trabajosgrado_codigo')
                trabajos_jurados = Trabajosgrado.objects.filter(codigo__in=jurado_filtrado)
                kwargs["queryset"] = Trabajosgrado.objects.filter(codigo__in=trabajos_jurados)
        return super(PropuestatgAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

#Define un modelo de administracion para Propuestas de trabajo de grado
class PropuestatgRevisorestAdmin(admin.ModelAdmin):
    list_display = ('id', 'propuestatg', 'revisorestecnicos')
    list_filter = ['id']
    search_fields = ['id']

    def add_view(self, *args, **kwargs):
        self.fields = ('propuestatg', 'revisorestecnicos')
        return super(PropuestatgRevisorestAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()


#Define un modelo de administracion para Revisores Tecnicos
class RevisorestecnicosAdmin(admin.ModelAdmin):
    list_display = ('id', 'concepto', 'docentes_dni')
    list_filter = ['id']
    search_fields = ['id']

    def add_view(self, *args, **kwargs):
        self.fields = ('docentes_dni', 'concepto')
        return super(RevisorestecnicosAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

#Define un modelo de administracion para Solicitudes pasantes
class SolicitudespasantesAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'empresaspasantes', 'concejocurricular', 'conceptossolicitudes', 'link', 'revisorestecnicos')
    list_filter = ['id']
    search_fields = ['id']

    def add_view(self, *args, **kwargs):
        self.fields = ('fecha', 'empresaspasantes', 'concejocurricular', 'conceptossolicitudes', 'revisorestecnicos', 'link')
        return super(SolicitudespasantesAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

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

    def add_view(self, *args, **kwargs):
        self.fields = ('fechapublicacion', 'fecharealizacion', 'hora','lugar' , 'nota', 'trabajosgrado_codigo')
        return super(SustentacionesAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "trabajosgrado_codigo":
            if request.user.tipo == Usuario.JURADO:
                jurado_filtrado = Jurados.objects.filter(docentes_dni=request.user.dni).values('trabajosgrado_codigo')
                trabajos_jurados = Trabajosgrado.objects.filter(codigo__in=jurado_filtrado)
                kwargs["queryset"] = Trabajosgrado.objects.filter(codigo__in=trabajos_jurados)
        return super(SustentacionesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

#Define un modelo de administracion para Tipodocente
class TipodocenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ['descripcion']
    search_fields = ['descripcion']

    def add_view(self, *args, **kwargs):
        self.fields = ('descripcion',)
        return super(TipodocenteAdmin, self).add_view(*args, **kwargs)
    """
    def formfield_for_dbfield(self, db_field, **kwargs):    
        if db_field.name == 'descripcion':
            kwargs['widget'] = forms.Select(choices=Usuario.TIPO_USUARIO[1:])  # en los tipos de docente no puede haber un tipo estudiante..
        return super(TipodocenteAdmin,self).formfield_for_dbfield(db_field,**kwargs)
    """
    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save() 

#Define un modelo de administracion para Tiposempresa
class TiposempresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    list_filter = ['descripcion']
    search_fields = ['descripcion']    

    def add_view(self, *args, **kwargs):
        self.fields = ('descripcion',)
        return super(TiposempresaAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save() 

#Define un modelo de administracion para Trabajosgrado
class TrabajosgradoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo', 'grupo_investigacion', 'nota_definitiva', 'docentes_director' )
    list_filter = ['codigo']
    """
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "docentes_director":
            kwargs["queryset"] = Docentes.objects.filter(tipodocente__descripcion=Usuario.DIRECTOR) #pk=tipoDocenteDirector.id)
        return super(TrabajosgradoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    """
    def save_model(self, request, obj, form, change):
        if not change:
            user = Usuario.objects.create_userRol(obj.docentes_director.dni, Usuario.DIRECTOR, obj.docentes_director.dni)
        obj.save()

    def queryset(self, request):
        qs = super(TrabajosgradoAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.tipo == Usuario.ASESOR:
            asesor_filtrado = Asesores.objects.filter(docentes_dni=request.user.dni).values('trabajosgrado_codigo')
            #trabajos_asesor = Trabajosgrado.objects.filter(codigo__in=asesor_filtrado)
            return qs.filter(codigo__in=asesor_filtrado)
        if request.user.tipo == Usuario.JURADO:
            jurado_filtrado = Jurados.objects.filter(docentes_dni=request.user.dni).values('trabajosgrado_codigo')
            return qs.filter(codigo__in=jurado_filtrado)
        return qs

#Define un modelo de administracion para Visistas
class VisitasAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'hora', 'coordinadorestg', 'empresaspasantes_nit' )
    list_filter = ['id']
    search_fields = ['id']

    def add_view(self, *args, **kwargs):
        self.fields = ('fecha', 'hora', 'coordinadorestg', 'empresaspasantes_nit')
        return super(VisitasAdmin, self).add_view(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id  = get_id_autoincremental(obj)
        obj.save()


"""
    UTILES
""" 
def get_id_autoincremental(model_object):
    ClassModel = model_object.__class__
    maximo = ClassModel.objects.all().aggregate(m=Max('id'))
    if maximo['m'] is not None:
        id  = maximo['m'] + 1
    else:
        id  = 1
    return id




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