# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlctom [appname]'
# into your database.
# encoding:utf-8
from __future__ import unicode_literals
from django.db import models

#Modelo de clase correspondiente a la tabla Asesores
class Asesores(models.Model):
    #Codigo del trabajo de grado a cargo del asesor
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo')
    #Identificacion del asesor
    docentes_dni = models.ForeignKey('Docentes', db_column='docentes_dni')
    #Fecha en que se ha asignado el asesor al trabajo de grado
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Asesores"
        managed = False
        db_table = 'asesores'

#Modelo de clase correspondiente a la tabla Aspectos
class Aspectos(models.Model):
    #Id del aspecto 
    id = models.BigIntegerField(primary_key=True)
    #Descripcion del aspectos de la calificacion del trabajo
    descripcion = models.CharField(max_length=20)
    #Porcentaje de nota que representa el aspecto
    porcentaje = models.DecimalField(max_digits=2, decimal_places=2)
    #Referencia a la evaluacion de este aspecto
    evaluacionestrabajogrado = models.ForeignKey('Evaluacionestrabajogrado')
    class Meta:
        verbose_name_plural = "Aspectos"
        managed = False
        db_table = 'aspectos'

#Modelo de clase correspondiente a la tabla Caracter
class Caracter(models.Model):
    #Id del caracter de evaluacion
    id = models.BigIntegerField(primary_key=True)
    #Descripcion del caracter evaluativo(Aprobatorio, meritorio o laureado)
    descripcion = models.CharField(max_length=15, blank=True)

    #El retorno a mostrar sera la descripcion del caracter
    def __unicode__(self):
        return self.descripcion
    class Meta:
        verbose_name_plural = "Caracter"
        managed = False
        db_table = 'caracter'

#Modelo de clase correspondiente a la tabla Concejocurricular
class Concejocurricular(models.Model):
    #Identificador unico del concejocurricular
    id = models.BigIntegerField(primary_key=True)
    #La fecha en que se ha creado el concejo
    fechacreacion = models.DateField()
    class Meta:
        verbose_name_plural = "Concejos Curriculares"
        managed = False
        db_table = 'concejocurricular'

#Modelo de clase correspondiente a la tabla Conceptossolicitudes
class Conceptossolicitudes(models.Model):
    #Identificador del concepto de solicitud
    id = models.BigIntegerField(primary_key=True)
    #Descripcion del concepto de la solicitud del trabajo
    descripcion = models.CharField(max_length=15)
    class Meta:
        verbose_name_plural = "Conceptos Solicitudes"
        managed = False
        db_table = 'conceptossolicitudes'

#Modelo de clase correspondiente a la tabla Conveniomarco
class Conveniomarco(models.Model):
    #Identificador del convenio marco entre empresas y universidad
    id = models.BigIntegerField(primary_key=True)

    #Fecha en que se aprobo el convenio
    fecha = models.DateField()
    #Estado del convenio
    activo = models.CharField(max_length=1, blank=True)
    #Nit de la empresa con que se ha hecho el convenio
    empresaspasantes_nit = models.ForeignKey('Empresaspasantes', db_column='empresaspasantes_nit')
    class Meta:
        verbose_name_plural = "Convenios Marco"
        managed = False
        db_table = 'conveniomarco'

#Modelo de clase correspondiente a la tabla Convocatorias
class Convocatorias(models.Model):
    #Identificador de la convocatoria
    id = models.BigIntegerField(primary_key=True)
    #Descripcion que detalla las condiciones de convocatoria
    descripcion = models.CharField(max_length=30, blank=True)
    #Fecha en que se inicia la convocatoria
    fechainicio = models.DateField()
    #Fecha en que se cierra la convocatoria
    fechalimite = models.DateField()
    #Referencia a la solicitud correspondiente de convocatoria
    solicitudespasantes = models.ForeignKey('Solicitudespasantes')
    class Meta:
        verbose_name_plural = "Convocatorias"
        managed = False
        db_table = 'convocatorias'

#Modelo de clase correspondiente a la tabla Coordinadorestg
class Coordinadorestg(models.Model):
    #Identificador del coordinador del trabajo de grado
    id = models.BigIntegerField(primary_key=True)
    #Identificacion como docente, del coordinador 
    docentes_dni = models.ForeignKey('Docentes', db_column='docentes_dni')
    #ano en que llevara la coordinacion
    anio = models.BigIntegerField(db_column='a\xf1o') # Field renamed to remove unsuitable characters.
    #Semestre en el cual sera coordinador
    semestreacademico = models.CharField(max_length=1)
    class Meta:
        verbose_name_plural = "Coordinadores Trabajos de Grado"
        managed = False
        db_table = 'coordinadorestg'

#Modelo de clase correspondiente a la tabla Criterios
class Criterios(models.Model):
    #Identificador del criterio emitido por el concejo
    id = models.BigIntegerField(primary_key=True)
    #Descripcion del criterio del trabajo (viable, no viable o aplazado)
    descripcion = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = "Criterios"
        managed = False
        db_table = 'criterios'

#Modelo de clase correspondiente a la tabla Criteriosaspectos
class Criteriosaspectos(models.Model):
    #Identificador de la tabla criteriosaspectos
    id = models.BigIntegerField(primary_key=True)
    #Descripcion de los criterios a tener en cuenta en los aspectos de evaluacion
    descripcion = models.CharField(max_length=30)
    #porcentaje que representa cada criterio del aspecto
    porcentaje = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    #Calificacion que tiene cada criterio por aspecto
    calificacion = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    #Referencia a los aspectos de cada criterio
    aspectos = models.ForeignKey(Aspectos)
    class Meta:
        verbose_name_plural = "Criterios Aspectos"
        managed = False
        db_table = 'criteriosaspectos'

#Modelo de clase correspondiente a la tabla Criteriosjurado
class Criteriosjurado(models.Model):
    #Identificador de los criterios del jurado
    id = models.BigIntegerField(primary_key=True)
    #Descripcion de los criterios del jurado
    descripcion = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = "Criterios Jurados"
        managed = False
        db_table = 'criteriosjurado'

#Modelo de clase correspondiente a la tabla Cronogramas
class Cronogramas(models.Model):
    #Identificador de los cronogramas
    id = models.BigIntegerField(primary_key=True)
    #Detalles de los eventos programados
    descripcion = models.CharField(max_length=30, blank=True)
    #Fecha inicial de la actividad
    fechainicio = models.DateField(blank=True, null=True)
    #Fecha final de la actividad
    fechafin = models.DateField(blank=True, null=True)
    #Trabajo de grado al que corresponde el cronograma
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo')
    class Meta:
        verbose_name_plural = "Cronogramas"
        managed = False
        db_table = 'cronogramas'

#Modelo de clase correspondiente a la tabla Docentes
class Docentes(models.Model):
    #Idenficacion personal del docente
    dni = models.IntegerField(primary_key=True)
    #Nombre del docente
    nombre = models.CharField(max_length=30)
    #Apellidos del docente
    apellidos = models.CharField(max_length=30)
    #Referencia al tipo de docente 
    tipodocente = models.ForeignKey('Tipodocente')

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Docentes"
        managed = False
        db_table = 'docentes'

#Modelo de clase correspondiente a la tabla DoncentesConsejocurricular
class DocentesConsejocurricular(models.Model):
    #Referencia al concejo curricular como intermediaacion con los proyectos
    concejocurricular = models.ForeignKey(Concejocurricular)
    #Referencia al docente a cargo de proyectos
    docentes_dni = models.ForeignKey(Docentes, db_column='docentes_dni')
    class Meta:
        verbose_name_plural = "Docentes Concejos Curriculares"
        managed = False
        db_table = 'docentes_consejocurricular'

#Modelo de clase correspondiente a la tabla Documentacion
class Documentacion(models.Model):
    #Identificador unico de la documentacion
    id = models.BigIntegerField(primary_key=True)
    #Fecha en que se produjo el documento
    fecha = models.DateField()
    #Asunto de que trata el documento
    asunto = models.CharField(max_length=30)
    #Campo para ingresar el contenido del documento
    descripcion = models.CharField(max_length=100)
    #Id del trabajo de grado sobre el que se hace la documentacion
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo')
    #Enlace web del documento
    link = models.CharField(max_length=20, blank=True)
    #Campo para referirse a otros documentos relacionados con el actual
    documentacion_alterna = models.ForeignKey('self', blank=True, null=True)
    class Meta:
        verbose_name_plural = "Documentaciones"
        managed = False
        db_table = 'documentacion'

#Modelo de clase correspondiente a la tabla Empresaspasantes
class Empresaspasantes(models.Model):
    #Campo del nit de la empresa
    nit = models.BigIntegerField(primary_key=True)
    #Nombre de la empresa pasante
    nombre = models.CharField(max_length=30)
    #Direccion de la empresa pasante
    direccion = models.CharField(max_length=30)
    #Referencia al tipo de empresa que solicita la pasantia
    tiposempresa = models.ForeignKey('Tiposempresa')
    class Meta:
        verbose_name_plural = "Empresas Pasantes"
        managed = False
        db_table = 'empresaspasantes'

#Modelo de clase correspondiente a la tabla Estudiantes
class Estudiantes(models.Model):
    #Identificacion unica del estudiante
    dni = models.BigIntegerField(primary_key=True)
    #Nombre del estudiante
    nombre = models.CharField(max_length=30)
    #Apellidos del estudiante
    apellidos = models.CharField(max_length=30)
    #Referencia al trabajo de grado que desarrollara
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo')
    class Meta:
        verbose_name_plural = "Estudiantes"
        managed = False
        db_table = 'estudiantes'

#Modelo de clase correspondiente a la tabla Evaluacionestrabajogrado
class Evaluacionestrabajogrado(models.Model):
    #Identificador unico de la evaluacion
    id = models.BigIntegerField(primary_key=True)
    #Campo que contiene la fecha de la evaluacion
    fecha = models.DateField()
    #Campo para la nota final de los aspectos de evaluacion
    nota_final_aspectos = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    #Referencia al caracter bajo el cual se realiza la evaluacion
    caracter = models.ForeignKey(Caracter)
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='Trabajosgrado_codigo')
    class Meta:
        verbose_name_plural = "Evaluaciones Trabajos de Grado"
        managed = False
        db_table = 'evaluacionestrabajogrado'

#Modelo de clase correspondiente a la tabla Historicocriteriospropuestas
class Historicocriteriospropuestas(models.Model):
    #Campo de referencia a los criterios que ha tenido el trabajo
    criterios = models.ForeignKey(Criterios)
    #Campo de referencia al concejo curricular
    concejocurricular = models.ForeignKey(Concejocurricular)
    #Fecha en que se ha emitido dicho criterio
    fecha = models.DateField()
    #Enlace web donde esta el historial de criterios
    link = models.CharField(max_length=20, blank=True)
    #Campo de referencia a la propuesta del trabajo
    proptg_revtproptg = models.ForeignKey('PropuestatgRevisorest')
    #Campo de referencia a los revisores tecnicos de la propuesta
    proptg_revt_revtec = models.ForeignKey('PropuestatgRevisorest', related_name="proptg_revt_revtec")
    class Meta:
        verbose_name_plural = "Historicos Criterios Propuestas"
        managed = False
        db_table = 'historicocriteriospropuestas'

#Modelo de clase correspondiente a la tabla InformefinalCriterios
class InformefinalCriterios(models.Model):
    #Fecha en que se emite el informe final 
    fecha = models.DateField()
    #Campo de referencia al informe final 
    informesfinales = models.ForeignKey('Informesfinales')
    #Campo donde se incluye los criterios que designa el jurado calificador
    criteriosjurado = models.ForeignKey(Criteriosjurado)
    #Referencia al jurado que emitio el informe
    jurados_trabajosgrado_codigo = models.ForeignKey('Jurados', db_column='jurados_trabajosgrado_codigo')
    #Referencia al docente que actua como jurado
    jurados_docentes_dni = models.ForeignKey('Jurados', db_column='jurados_docentes_dni', related_name="jurados_docentes_dni")
    #Enlace web sobre el detalle de los criterios del informe final 
    link = models.CharField(max_length=20, blank=True)
    class Meta:
        verbose_name_plural = "Informes Finales Criterios"
        managed = False
        db_table = 'informefinal_criterios'

#Modelo de clase correspondiente a la tabla Informesfinales
class Informesfinales(models.Model):
    #Identificador unico del informe final
    id = models.BigIntegerField(primary_key=True)
    #Campo para el titulo del informe final
    titulo = models.CharField(max_length=30, blank=True)
    #Fecha en que se realiza el informe final 
    fecha = models.DateField()
    #Referencia al consejo curricular
    concejocurricular = models.ForeignKey(Concejocurricular)
    #Campo de referencia a los coordinadores a cargo del trabajo de grado
    coordinadorestg = models.ForeignKey(Coordinadorestg)
    #Campo que referencia el trabajo sobre el que se emite el informe final
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo', unique=True)
    #Enlace web detallado de la descripcion del informe final
    link = models.CharField(max_length=20, blank=True)
    class Meta:
        verbose_name_plural = "Informes Finales"
        managed = False
        db_table = 'informesfinales'

#Modelo de clase correspondiente a la tabla Informesperiodicos
class Informesperiodicos(models.Model):
    #Identificador unico de los informes periodicos de la pasantia
    id = models.BigIntegerField(primary_key=True)
    #Enlace con el informe detallado de la pasantia
    link = models.CharField(max_length=30)
    #Campo con la fecha en que se realiza el informe periodico
    fecha = models.DateField()
    #Referencia a la pasantia a que alude el informe
    pasantias_trabajosgrado_codigo = models.ForeignKey('Pasantias', db_column='pasantias_trabajosgrado_codigo')
    class Meta:
        verbose_name_plural = "Informes Periodicos"
        managed = False
        db_table = 'informesperiodicos'

#Modelo de clase correspondiente a la tabla Jurados
class Jurados(models.Model):
    #Referencia al trabajo de grado que calificara el jurado
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo')
    #Campo referente a la identificacion del docente que servira de jurado
    docentes_dni = models.ForeignKey(Docentes, db_column='docentes_dni')
    #Persona que sera el presidente de la terna del jurado calificador
    presidente = models.CharField(max_length=1, blank=True)
    #Campo de referencia al concejo curricular
    concejocurricular = models.ForeignKey(Concejocurricular)
    #Fecha de asignacion de jurados
    fecha = models.DateField(blank=True, null=True)
    class Meta:
        verbose_name_plural = "Jurados"
        managed = False
        db_table = 'jurados'

#Modelo de clase correspondiente a la tabla Modalidadespasantia
class Modalidadespasantia(models.Model):
    #Identificador unico de la modalidad de la pasantia
    id = models.BigIntegerField(primary_key=True)
    #Descripcion de la modalidad de pasantia (laboral, proyeccion social, internacional o investigacion)
    descripcion = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = "Modalidades Pasantia"
        managed = False
        db_table = 'modalidadespasantia'

#Modelo de clase correspondiente a la tabla Modadiladestg
class Modalidadestg(models.Model):
    #Identificador de la modalidad del trabajo de grado
    id = models.BigIntegerField(primary_key=True)
    #Campo que representa la modalidad del trabajo
    descripcion = models.CharField(max_length=30, blank=True)
    #Referencia al trabajo de grado especificado por la modalidad
    trabajogrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajogrado_codigo')
    class Meta:
        verbose_name_plural = "Modalidades Trabajos de Grado"
        managed = False
        db_table = 'modalidadestg'

#Modelo de clase correspondiente a la tabla Pasantias
class Pasantias(models.Model):
    #Identificador unico de la pasantia
    codigo = models.BigIntegerField(primary_key=True)
    #Referencia al trabajo de grado presentado por el(los) estudiante(s)
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo', unique=True)
    #Empresa pasante que solicita la pasantia
    empresaspasantes = models.ForeignKey(Empresaspasantes)
    #Campo que referencia la modalidad de la pasantia
    modalidadespasantia = models.ForeignKey(Modalidadespasantia)
    #Referencia de la previa propuesta de pasantia
    propuestaspasantias_id = models.BigIntegerField(unique=True)
    class Meta:
        verbose_name_plural = "Pasantias"
        managed = False
        db_table = 'pasantias'

#Modelo de clase correspondiente a la tabla Propuestatg
class Propuestatg(models.Model):
    #Identificador unico de la propuesta de trabajo de grado 
    id = models.BigIntegerField(primary_key=True)
    #Campo para elt titulo de la propuesta del trabajo de grado 
    titulo = models.CharField(max_length=30, blank=True)
    #Fecha en que se presenta la propuesta
    fechapresentacion = models.DateField()
    #Referencia al coordinador que esta a cargo de la propuesta
    coordinadorestg = models.ForeignKey(Coordinadorestg)
    #Enlace con la especificacion detallada de la propuesta
    link = models.CharField(max_length=20, blank=True)
    #Referencia al trabajo de grado al que pertenece la propuesta
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo')
    class Meta:
        verbose_name_plural = "Propuestas Trabajos de Grado"
        managed = False
        db_table = 'propuestatg'

#Modelo de clase correspondiente a la tabla PropuestatgRevisorest
class PropuestatgRevisorest(models.Model):
    #Campo que se refiere a la propuesta que sera revisada
    propuestatg = models.ForeignKey(Propuestatg)
    #Campo de referencia a los revisores tecnicos encargados de evaluar la propuesta
    revisorestecnicos = models.ForeignKey('Revisorestecnicos')
    class Meta:
        verbose_name_plural = "Propuestas_Trabajos de Grado_Revisores Tecnicos"
        managed = False
        db_table = 'propuestatg_revisorest'

#Modelo de clase correspondiente a la tabla Revisorestecnicos
class Revisorestecnicos(models.Model):
    #Identificador unico de cada revisor tecnico
    id = models.BigIntegerField(primary_key=True)
    #El concepto indica la aprobacion o desaprobacion de la propuesta enviada
    concepto = models.CharField(max_length=20, blank=True)
    #Identificacion del docente que realizara la revision tecnica
    docentes_dni = models.ForeignKey(Docentes, db_column='docentes_dni')
    class Meta:
        verbose_name_plural = "Revisores Tecnicos"
        managed = False
        db_table = 'revisorestecnicos'

#Modelo de clase correspondiente a la tabla Solicitudespasantes
class Solicitudespasantes(models.Model):
    #Identificador de la solicitud de pasantes
    id = models.BigIntegerField(primary_key=True)
    #fecha en que se realiza la solicitud de estudiantes para pasantias
    fecha = models.DateField()
    #Empresa encargada de realizar la solicitud de pasantes
    empresaspasantes = models.ForeignKey(Empresaspasantes)
    #Referencia al concejo curricular del programa
    concejocurricular = models.ForeignKey(Concejocurricular)
    #Referencia sobre el concepto que tiene la solicitud
    conceptossolicitudes = models.ForeignKey(Conceptossolicitudes)
    #Enlace web con la solicitud detallada de pasantes
    link = models.CharField(max_length=20, blank=True)
    #Campo de llave foranea de los revisores encargados de la solicitud
    revisorestecnicos = models.ForeignKey(Revisorestecnicos, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Solicitudes Pasantes"
        managed = False
        db_table = 'solicitudespasantes'

#Modelo de clase correspondiente a la tabla Supervisoresempresas
class Supervisoresempresas(models.Model):
    #Identificacion personal del supervisor de la empresa donde se realizara la pasantia
    dni = models.BigIntegerField(primary_key=True)
    #Nombre del supervisor de la empresa
    nombre = models.CharField(max_length=30)
    #Apellidos del supervisor de la empresa
    apellidos = models.CharField(max_length=30, blank=True)
    #Cargo que tiene el supervisor al interior de la empresa
    cargo = models.CharField(max_length=20, blank=True)
    #Foranea que indica la empresa a la cual pertenece el supervisor
    empresaspasantes_nit = models.ForeignKey(Empresaspasantes, db_column='empresaspasantes_nit')
    class Meta:
        verbose_name_plural = "Supervisores Empresas"
        managed = False
        db_table = 'supervisoresempresas'

#Modelo de clase correspondiente a la tabla Sustentaciones
class Sustentaciones(models.Model):
    #Identificador unico de la sustentacion
    id = models.BigIntegerField(primary_key=True)
    #Fecha en la que se publica la programacion de sustentacion
    fechapublicacion = models.DateField(blank=True, null=True)
    #Fecha en que el estudiante realiza la sustentacion 
    fecharealizacion = models.DateField()
    #Campo que indica la hora en que el estudiante debe sustentar
    hora = models.DateField()
    #Campo que especifica el lugar donde se realizara la sustentacion
    lugar = models.CharField(max_length=30)
    #Calificacion obtenida debido a la sustentacion
    nota = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    #Foranea del trabajo de grado sustentado
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo', unique=True)
    class Meta:
        verbose_name_plural = "Sustentaciones"
        managed = False
        db_table = 'sustentaciones'

#Modelo de clase correspondiente a la tabla Tipodocente
class Tipodocente(models.Model):
    #Identificador unico del tipo de docente
    id = models.IntegerField(primary_key=True)
    #Campo que indica la clasificacion del docente (planta, catedratico, ocasional, externo)
    descripcion = models.CharField(max_length=30)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Tipos de Docente"
        managed = False
        db_table = 'tipodocente'

#Modelo de clase correspondiente a la tabla Tiposempresa
class Tiposempresa(models.Model):
    #Identificador unico del tipo de empresa
    id = models.BigIntegerField(primary_key=True)
    #Campo que indica si la empresa es publica o privada
    descripcion = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = "Tipos de Empresa"
        managed = False
        db_table = 'tiposempresa'

#Modelo de clase correspondiente a la tabla Trabajosgrado
class Trabajosgrado(models.Model):
    #Codigo unico del trabajo de grado
    codigo = models.BigIntegerField(primary_key=True)
    #Campo para el titulo del trabajo
    titulo = models.CharField(max_length=30)
    #Campo para una letra indicando si el trabajo de grado pertenece a un grupo de investigacion o si es mediante otra modalidad
    grupo_investigacion = models.CharField(max_length=30, blank=True)
    #Campo con la calificacion cuantitativa final del trabajo de grado
    nota_definitiva = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    #Referencia al docente que sera a su vez director del trabajo
    docentes_director = models.ForeignKey(Docentes, db_column='docentes_director')
    class Meta:
        verbose_name_plural = "Trabajos de Grado"
        managed = False
        db_table = 'trabajosgrado'

#Modelo de clase correspondiente a la tabla Visitas
class Visitas(models.Model):
    #Identificador unico de cada visita hecha por la empresa pasante
    id = models.BigIntegerField(primary_key=True)
    #Fecha en que se realizo la visita
    fecha = models.DateField()
    #Hora en que realizaron la visita los representantes de la empresa 
    hora = models.DateField()
    #Referencia el docente como coordinador del trabajo 
    coordinadorestg = models.ForeignKey(Coordinadorestg)
    #Identificacion de la empresa pasante que envio personal para realizar la visita
    empresaspasantes_nit = models.ForeignKey(Empresaspasantes, db_column='empresaspasantes_nit')
    class Meta:
        verbose_name_plural = "Visitas"
        managed = False
        db_table = 'visitas'