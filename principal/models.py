# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
#encoding:utf-8
from __future__ import unicode_literals
from django.db import models

class Asesores(models.Model):
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo')
    docentes_dni = models.ForeignKey('Docentes', db_column='docentes_dni')
    fecha = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'asesores'

class Aspectos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    porcentaje = models.DecimalField(max_digits=2, decimal_places=2)
    evaluacionestrabajogrado = models.ForeignKey('Evaluacionestrabajogrado')
    class Meta:
        managed = False
        db_table = 'aspectos'

class Caracter(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=15, blank=True)
    class Meta:
        managed = False
        db_table = 'caracter'

class Concejocurricular(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fechacreacion = models.DateField()
    class Meta:
        managed = False
        db_table = 'concejocurricular'

class Conceptossolicitudes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=15)
    class Meta:
        managed = False
        db_table = 'conceptossolicitudes'

class Conveniomarco(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    activo = models.CharField(max_length=1, blank=True)
    empresaspasantes_nit = models.ForeignKey('Empresaspasantes', db_column='empresaspasantes_nit')
    class Meta:
        managed = False
        db_table = 'conveniomarco'

class Convocatorias(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30, blank=True)
    fechainicio = models.DateField()
    fechalimite = models.DateField()
    solicitudespasantes = models.ForeignKey('Solicitudespasantes')
    class Meta:
        managed = False
        db_table = 'convocatorias'

class Coordinadorestg(models.Model):
    id = models.BigIntegerField(primary_key=True)
    docentes_dni = models.ForeignKey('Docentes', db_column='docentes_dni')
    a_o = models.BigIntegerField(db_column='a\xf1o') # Field renamed to remove unsuitable characters.
    semestreacademico = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'coordinadorestg'

class Criterios(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'criterios'

class Criteriosaspectos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)
    porcentaje = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    calificacion = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    aspectos = models.ForeignKey(Aspectos)
    class Meta:
        managed = False
        db_table = 'criteriosaspectos'

class Criteriosjurado(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'criteriosjurado'

class Cronogramas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30, blank=True)
    fechainicio = models.DateField(blank=True, null=True)
    fechafin = models.DateField(blank=True, null=True)
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo')
    class Meta:
        managed = False
        db_table = 'cronogramas'

class Docentes(models.Model):
    dni = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    tipodocente = models.ForeignKey('Tipodocente')
    class Meta:
        managed = False
        db_table = 'docentes'

class DocentesConsejocurricular(models.Model):
    concejocurricular = models.ForeignKey(Concejocurricular)
    docentes_dni = models.ForeignKey(Docentes, db_column='docentes_dni')
    class Meta:
        managed = False
        db_table = 'docentes_consejocurricular'

class Documentacion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    asunto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo')
    link = models.CharField(max_length=20, blank=True)
    documentacion_alterna = models.ForeignKey('self', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'documentacion'

class Empresaspasantes(models.Model):
    nit = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    tiposempresa = models.ForeignKey('Tiposempresa')
    class Meta:
        managed = False
        db_table = 'empresaspasantes'

class Estudiantes(models.Model):
    dni = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo')
    class Meta:
        managed = False
        db_table = 'estudiantes'

class Evaluacionestrabajogrado(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    nota_final_aspectos = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    caracter = models.ForeignKey(Caracter)
    class Meta:
        managed = False
        db_table = 'evaluacionestrabajogrado'

class Historicocriteriospropuestas(models.Model):
    criterios = models.ForeignKey(Criterios)
    concejocurricular = models.ForeignKey(Concejocurricular)
    fecha = models.DateField()
    link = models.CharField(max_length=20, blank=True)
    proptg_revtproptg = models.ForeignKey('PropuestatgRevisorest')
    proptg_revt_revtec = models.ForeignKey('PropuestatgRevisorest', related_name="proptg_revt_revtec")
    class Meta:
        managed = False
        db_table = 'historicocriteriospropuestas'

class InformefinalCriterios(models.Model):
    fecha = models.DateField()
    informesfinales = models.ForeignKey('Informesfinales')
    criteriosjurado = models.ForeignKey(Criteriosjurado)
    jurados_trabajosgrado_codigo = models.ForeignKey('Jurados', db_column='jurados_trabajosgrado_codigo')
    jurados_docentes_dni = models.ForeignKey('Jurados', db_column='jurados_docentes_dni', related_name="jurados_docentes_dni")
    link = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'informefinal_criterios'

class Informesfinales(models.Model):
    id = models.BigIntegerField(primary_key=True)
    titulo = models.CharField(max_length=30, blank=True)
    fecha = models.DateField()
    concejocurricular = models.ForeignKey(Concejocurricular)
    coordinadorestg = models.ForeignKey(Coordinadorestg)
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo', unique=True)
    link = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'informesfinales'

class Informesperiodicos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    link = models.CharField(max_length=30)
    fecha = models.DateField()
    pasantias_trabajosgrado_codigo = models.ForeignKey('Pasantias', db_column='pasantias_trabajosgrado_codigo')
    class Meta:
        managed = False
        db_table = 'informesperiodicos'

class Jurados(models.Model):
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo')
    docentes_dni = models.ForeignKey(Docentes, db_column='docentes_dni')
    presidente = models.CharField(max_length=1, blank=True)
    concejocurricular = models.ForeignKey(Concejocurricular)
    fecha = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'jurados'

class Modalidadespasantia(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'modalidadespasantia'

class Modalidadestg(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30, blank=True)
    trabajogrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajogrado_codigo')
    class Meta:
        managed = False
        db_table = 'modalidadestg'

class Pasantias(models.Model):
    codigo = models.BigIntegerField(primary_key=True)
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo', unique=True)
    empresaspasantes = models.ForeignKey(Empresaspasantes)
    modalidadespasantia = models.ForeignKey(Modalidadespasantia)
    propuestaspasantias_id = models.BigIntegerField(unique=True)
    class Meta:
        managed = False
        db_table = 'pasantias'

class Propuestatg(models.Model):
    id = models.BigIntegerField(primary_key=True)
    titulo = models.CharField(max_length=30, blank=True)
    fechapresentacion = models.DateField()
    coordinadorestg = models.ForeignKey(Coordinadorestg)
    link = models.CharField(max_length=20, blank=True)
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo')
    class Meta:
        managed = False
        db_table = 'propuestatg'

class PropuestatgRevisorest(models.Model):
    propuestatg = models.ForeignKey(Propuestatg)
    revisorestecnicos = models.ForeignKey('Revisorestecnicos')
    class Meta:
        managed = False
        db_table = 'propuestatg_revisorest'

class Revisorestecnicos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    concepto = models.CharField(max_length=20, blank=True)
    docentes_dni = models.ForeignKey(Docentes, db_column='docentes_dni')
    class Meta:
        managed = False
        db_table = 'revisorestecnicos'

class Solicitudespasantes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    empresaspasantes = models.ForeignKey(Empresaspasantes)
    concejocurricular = models.ForeignKey(Concejocurricular)
    conceptossolicitudes = models.ForeignKey(Conceptossolicitudes)
    link = models.CharField(max_length=20, blank=True)
    revisorestecnicos = models.ForeignKey(Revisorestecnicos, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'solicitudespasantes'

class Supervisoresempresas(models.Model):
    dni = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30, blank=True)
    cargo = models.CharField(max_length=20, blank=True)
    empresaspasantes_nit = models.ForeignKey(Empresaspasantes, db_column='empresaspasantes_nit')
    class Meta:
        managed = False
        db_table = 'supervisoresempresas'

class Sustentaciones(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fechapublicacion = models.DateField(blank=True, null=True)
    fecharealizacion = models.DateField()
    hora = models.DateField()
    lugar = models.CharField(max_length=30)
    nota = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    trabajosgrado_codigo = models.ForeignKey('Trabajosgrado', db_column='trabajosgrado_codigo', unique=True)
    class Meta:
        managed = False
        db_table = 'sustentaciones'

class Tipodocente(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'tipodocente'

class Tiposempresa(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'tiposempresa'

class Trabajosgrado(models.Model):
    codigo = models.BigIntegerField(primary_key=True)
    titulo = models.CharField(max_length=30)
    grupo_investigacion = models.CharField(max_length=30, blank=True)
    nota_definitiva = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    docentes_director = models.ForeignKey(Docentes, db_column='docentes_director')
    evaluacionestrabajogrado = models.ForeignKey(Evaluacionestrabajogrado)
    class Meta:
        managed = False
        db_table = 'trabajosgrado'

class Visitas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    hora = models.DateField()
    coordinadorestg = models.ForeignKey(Coordinadorestg)
    empresaspasantes_nit = models.ForeignKey(Empresaspasantes, db_column='empresaspasantes_nit')
    class Meta:
        managed = False
        db_table = 'visitas'

