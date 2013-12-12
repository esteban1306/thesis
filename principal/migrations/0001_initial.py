# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Asesores'
        db.create_table(u'asesores', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trabajosgrado_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Trabajosgrado'], db_column=u'trabajosgrado_codigo')),
            ('docentes_dni', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Docentes'], db_column=u'docentes_dni')),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'principal', ['Asesores'])

        # Adding unique constraint on 'Asesores', fields ['trabajosgrado_codigo', 'docentes_dni']
        db.create_unique(u'asesores', [u'trabajosgrado_codigo', u'docentes_dni'])

        # Adding model 'Aspectos'
        db.create_table(u'aspectos', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('porcentaje', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=2)),
            ('evaluacionestrabajogrado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Evaluacionestrabajogrado'])),
        ))
        db.send_create_signal(u'principal', ['Aspectos'])

        # Adding model 'Caracter'
        db.create_table(u'caracter', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal(u'principal', ['Caracter'])

        # Adding model 'Concejocurricular'
        db.create_table(u'concejocurricular', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('fechacreacion', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'principal', ['Concejocurricular'])

        # Adding model 'Conceptossolicitudes'
        db.create_table(u'conceptossolicitudes', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'principal', ['Conceptossolicitudes'])

        # Adding model 'Conveniomarco'
        db.create_table(u'conveniomarco', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('activo', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('empresaspasantes_nit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Empresaspasantes'], db_column=u'empresaspasantes_nit')),
        ))
        db.send_create_signal(u'principal', ['Conveniomarco'])

        # Adding model 'Convocatorias'
        db.create_table(u'convocatorias', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('fechainicio', self.gf('django.db.models.fields.DateField')()),
            ('fechalimite', self.gf('django.db.models.fields.DateField')()),
            ('solicitudespasantes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Solicitudespasantes'])),
        ))
        db.send_create_signal(u'principal', ['Convocatorias'])

        # Adding model 'Coordinadorestg'
        db.create_table(u'coordinadorestg', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('docentes_dni', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Docentes'], db_column=u'docentes_dni')),
            ('anio', self.gf('django.db.models.fields.BigIntegerField')(db_column=u'a\xf1o')),
            ('semestreacademico', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'principal', ['Coordinadorestg'])

        # Adding model 'Criterios'
        db.create_table(u'criterios', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'principal', ['Criterios'])

        # Adding model 'Criteriosaspectos'
        db.create_table(u'criteriosaspectos', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('porcentaje', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=2, blank=True)),
            ('calificacion', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=2, blank=True)),
            ('aspectos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Aspectos'])),
        ))
        db.send_create_signal(u'principal', ['Criteriosaspectos'])

        # Adding model 'Criteriosjurado'
        db.create_table(u'criteriosjurado', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'principal', ['Criteriosjurado'])

        # Adding model 'Cronogramas'
        db.create_table(u'cronogramas', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('fechainicio', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fechafin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('trabajosgrado_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Trabajosgrado'], db_column=u'trabajosgrado_codigo')),
        ))
        db.send_create_signal(u'principal', ['Cronogramas'])

        # Adding model 'Docentes'
        db.create_table(u'docentes', (
            ('dni', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('tipodocente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Tipodocente'])),
        ))
        db.send_create_signal(u'principal', ['Docentes'])

        # Adding model 'DocentesConsejocurricular'
        db.create_table(u'docentes_consejocurricular', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('concejocurricular', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Concejocurricular'])),
            ('docentes_dni', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Docentes'], db_column=u'docentes_dni')),
        ))
        db.send_create_signal(u'principal', ['DocentesConsejocurricular'])

        # Adding model 'Documentacion'
        db.create_table(u'documentacion', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('asunto', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('trabajosgrado_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Trabajosgrado'], db_column=u'trabajosgrado_codigo')),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('documentacion_alterna', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Documentacion'], null=True, blank=True)),
        ))
        db.send_create_signal(u'principal', ['Documentacion'])

        # Adding model 'Empresaspasantes'
        db.create_table(u'empresaspasantes', (
            ('nit', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('tiposempresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Tiposempresa'])),
        ))
        db.send_create_signal(u'principal', ['Empresaspasantes'])

        # Adding model 'Estudiantes'
        db.create_table(u'estudiantes', (
            ('dni', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('trabajosgrado_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Trabajosgrado'], db_column=u'trabajosgrado_codigo')),
        ))
        db.send_create_signal(u'principal', ['Estudiantes'])

        # Adding model 'Evaluacionestrabajogrado'
        db.create_table(u'evaluacionestrabajogrado', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('nota_final_aspectos', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=2, blank=True)),
            ('caracter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Caracter'])),
            ('trabajosgrado_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Trabajosgrado'], db_column=u'Trabajosgrado_codigo')),
        ))
        db.send_create_signal(u'principal', ['Evaluacionestrabajogrado'])

        # Adding model 'Historicocriteriospropuestas'
        db.create_table(u'historicocriteriospropuestas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('criterios', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Criterios'])),
            ('concejocurricular', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Concejocurricular'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('proptg_revtproptg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.PropuestatgRevisorest'])),
            ('proptg_revt_revtec', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'proptg_revt_revtec', to=orm['principal.PropuestatgRevisorest'])),
        ))
        db.send_create_signal(u'principal', ['Historicocriteriospropuestas'])

        # Adding model 'InformefinalCriterios'
        db.create_table(u'informefinal_criterios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('informesfinales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Informesfinales'])),
            ('criteriosjurado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Criteriosjurado'])),
            ('jurados_trabajosgrado_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Jurados'], db_column=u'jurados_trabajosgrado_codigo')),
            ('jurados_docentes_dni', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'jurados_docentes_dni', db_column=u'jurados_docentes_dni', to=orm['principal.Jurados'])),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'principal', ['InformefinalCriterios'])

        # Adding model 'Informesfinales'
        db.create_table(u'informesfinales', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('concejocurricular', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Concejocurricular'])),
            ('coordinadorestg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Coordinadorestg'])),
            ('trabajosgrado_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Trabajosgrado'], unique=True, db_column=u'trabajosgrado_codigo')),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'principal', ['Informesfinales'])

        # Adding model 'Informesperiodicos'
        db.create_table(u'informesperiodicos', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('pasantias_trabajosgrado_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Pasantias'], db_column=u'pasantias_trabajosgrado_codigo')),
        ))
        db.send_create_signal(u'principal', ['Informesperiodicos'])

        # Adding model 'Jurados'
        db.create_table(u'jurados', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trabajosgrado_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Trabajosgrado'], db_column=u'trabajosgrado_codigo')),
            ('docentes_dni', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Docentes'], db_column=u'docentes_dni')),
            ('presidente', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('concejocurricular', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Concejocurricular'])),
            ('fecha', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'principal', ['Jurados'])

        # Adding model 'Modalidadespasantia'
        db.create_table(u'modalidadespasantia', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'principal', ['Modalidadespasantia'])

        # Adding model 'Modalidadestg'
        db.create_table(u'modalidadestg', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('trabajogrado_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Trabajosgrado'], db_column=u'trabajogrado_codigo')),
        ))
        db.send_create_signal(u'principal', ['Modalidadestg'])

        # Adding model 'Pasantias'
        db.create_table(u'pasantias', (
            ('codigo', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('trabajosgrado_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Trabajosgrado'], unique=True, db_column=u'trabajosgrado_codigo')),
            ('empresaspasantes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Empresaspasantes'])),
            ('modalidadespasantia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Modalidadespasantia'])),
            ('propuestaspasantias_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True)),
        ))
        db.send_create_signal(u'principal', ['Pasantias'])

        # Adding model 'Propuestatg'
        db.create_table(u'propuestatg', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('fechapresentacion', self.gf('django.db.models.fields.DateField')()),
            ('coordinadorestg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Coordinadorestg'])),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('trabajosgrado_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Trabajosgrado'], db_column=u'trabajosgrado_codigo')),
        ))
        db.send_create_signal(u'principal', ['Propuestatg'])

        # Adding model 'PropuestatgRevisorest'
        db.create_table(u'propuestatg_revisorest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('propuestatg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Propuestatg'])),
            ('revisorestecnicos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Revisorestecnicos'])),
        ))
        db.send_create_signal(u'principal', ['PropuestatgRevisorest'])

        # Adding model 'Revisorestecnicos'
        db.create_table(u'revisorestecnicos', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('concepto', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('docentes_dni', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Docentes'], db_column=u'docentes_dni')),
        ))
        db.send_create_signal(u'principal', ['Revisorestecnicos'])

        # Adding model 'Solicitudespasantes'
        db.create_table(u'solicitudespasantes', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('empresaspasantes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Empresaspasantes'])),
            ('concejocurricular', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Concejocurricular'])),
            ('conceptossolicitudes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Conceptossolicitudes'])),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('revisorestecnicos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Revisorestecnicos'], null=True, blank=True)),
        ))
        db.send_create_signal(u'principal', ['Solicitudespasantes'])

        # Adding model 'Supervisoresempresas'
        db.create_table(u'supervisoresempresas', (
            ('dni', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('empresaspasantes_nit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Empresaspasantes'], db_column=u'empresaspasantes_nit')),
        ))
        db.send_create_signal(u'principal', ['Supervisoresempresas'])

        # Adding model 'Sustentaciones'
        db.create_table(u'sustentaciones', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('fechapublicacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecharealizacion', self.gf('django.db.models.fields.DateField')()),
            ('hora', self.gf('django.db.models.fields.DateField')()),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nota', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=2, blank=True)),
            ('trabajosgrado_codigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Trabajosgrado'], unique=True, db_column=u'trabajosgrado_codigo')),
        ))
        db.send_create_signal(u'principal', ['Sustentaciones'])

        # Adding model 'Tipodocente'
        db.create_table(u'tipodocente', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'principal', ['Tipodocente'])

        # Adding model 'Tiposempresa'
        db.create_table(u'tiposempresa', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'principal', ['Tiposempresa'])

        # Adding model 'Trabajosgrado'
        db.create_table(u'trabajosgrado', (
            ('codigo', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('grupo_investigacion', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('nota_definitiva', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=2, blank=True)),
            ('docentes_director', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Docentes'], db_column=u'docentes_director')),
        ))
        db.send_create_signal(u'principal', ['Trabajosgrado'])

        # Adding model 'Visitas'
        db.create_table(u'visitas', (
            ('id', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('hora', self.gf('django.db.models.fields.DateField')()),
            ('coordinadorestg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Coordinadorestg'])),
            ('empresaspasantes_nit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Empresaspasantes'], db_column=u'empresaspasantes_nit')),
        ))
        db.send_create_signal(u'principal', ['Visitas'])


    def backwards(self, orm):
        # Removing unique constraint on 'Asesores', fields ['trabajosgrado_codigo', 'docentes_dni']
        db.delete_unique(u'asesores', [u'trabajosgrado_codigo', u'docentes_dni'])

        # Deleting model 'Asesores'
        db.delete_table(u'asesores')

        # Deleting model 'Aspectos'
        db.delete_table(u'aspectos')

        # Deleting model 'Caracter'
        db.delete_table(u'caracter')

        # Deleting model 'Concejocurricular'
        db.delete_table(u'concejocurricular')

        # Deleting model 'Conceptossolicitudes'
        db.delete_table(u'conceptossolicitudes')

        # Deleting model 'Conveniomarco'
        db.delete_table(u'conveniomarco')

        # Deleting model 'Convocatorias'
        db.delete_table(u'convocatorias')

        # Deleting model 'Coordinadorestg'
        db.delete_table(u'coordinadorestg')

        # Deleting model 'Criterios'
        db.delete_table(u'criterios')

        # Deleting model 'Criteriosaspectos'
        db.delete_table(u'criteriosaspectos')

        # Deleting model 'Criteriosjurado'
        db.delete_table(u'criteriosjurado')

        # Deleting model 'Cronogramas'
        db.delete_table(u'cronogramas')

        # Deleting model 'Docentes'
        db.delete_table(u'docentes')

        # Deleting model 'DocentesConsejocurricular'
        db.delete_table(u'docentes_consejocurricular')

        # Deleting model 'Documentacion'
        db.delete_table(u'documentacion')

        # Deleting model 'Empresaspasantes'
        db.delete_table(u'empresaspasantes')

        # Deleting model 'Estudiantes'
        db.delete_table(u'estudiantes')

        # Deleting model 'Evaluacionestrabajogrado'
        db.delete_table(u'evaluacionestrabajogrado')

        # Deleting model 'Historicocriteriospropuestas'
        db.delete_table(u'historicocriteriospropuestas')

        # Deleting model 'InformefinalCriterios'
        db.delete_table(u'informefinal_criterios')

        # Deleting model 'Informesfinales'
        db.delete_table(u'informesfinales')

        # Deleting model 'Informesperiodicos'
        db.delete_table(u'informesperiodicos')

        # Deleting model 'Jurados'
        db.delete_table(u'jurados')

        # Deleting model 'Modalidadespasantia'
        db.delete_table(u'modalidadespasantia')

        # Deleting model 'Modalidadestg'
        db.delete_table(u'modalidadestg')

        # Deleting model 'Pasantias'
        db.delete_table(u'pasantias')

        # Deleting model 'Propuestatg'
        db.delete_table(u'propuestatg')

        # Deleting model 'PropuestatgRevisorest'
        db.delete_table(u'propuestatg_revisorest')

        # Deleting model 'Revisorestecnicos'
        db.delete_table(u'revisorestecnicos')

        # Deleting model 'Solicitudespasantes'
        db.delete_table(u'solicitudespasantes')

        # Deleting model 'Supervisoresempresas'
        db.delete_table(u'supervisoresempresas')

        # Deleting model 'Sustentaciones'
        db.delete_table(u'sustentaciones')

        # Deleting model 'Tipodocente'
        db.delete_table(u'tipodocente')

        # Deleting model 'Tiposempresa'
        db.delete_table(u'tiposempresa')

        # Deleting model 'Trabajosgrado'
        db.delete_table(u'trabajosgrado')

        # Deleting model 'Visitas'
        db.delete_table(u'visitas')


    models = {
        u'principal.asesores': {
            'Meta': {'unique_together': "((u'trabajosgrado_codigo', u'docentes_dni'),)", 'object_name': 'Asesores', 'db_table': "u'asesores'"},
            'docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_dni'"}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.aspectos': {
            'Meta': {'object_name': 'Aspectos', 'db_table': "u'aspectos'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'evaluacionestrabajogrado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Evaluacionestrabajogrado']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'porcentaje': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '2'})
        },
        u'principal.caracter': {
            'Meta': {'object_name': 'Caracter', 'db_table': "u'caracter'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.concejocurricular': {
            'Meta': {'object_name': 'Concejocurricular', 'db_table': "u'concejocurricular'"},
            'fechacreacion': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.conceptossolicitudes': {
            'Meta': {'object_name': 'Conceptossolicitudes', 'db_table': "u'conceptossolicitudes'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.conveniomarco': {
            'Meta': {'object_name': 'Conveniomarco', 'db_table': "u'conveniomarco'"},
            'activo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'empresaspasantes_nit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Empresaspasantes']", 'db_column': "u'empresaspasantes_nit'"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.convocatorias': {
            'Meta': {'object_name': 'Convocatorias', 'db_table': "u'convocatorias'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'fechainicio': ('django.db.models.fields.DateField', [], {}),
            'fechalimite': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'solicitudespasantes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Solicitudespasantes']"})
        },
        u'principal.coordinadorestg': {
            'Meta': {'object_name': 'Coordinadorestg', 'db_table': "u'coordinadorestg'"},
            'anio': ('django.db.models.fields.BigIntegerField', [], {'db_column': "u'a\\xf1o'"}),
            'docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_dni'"}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'semestreacademico': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'principal.criterios': {
            'Meta': {'object_name': 'Criterios', 'db_table': "u'criterios'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.criteriosaspectos': {
            'Meta': {'object_name': 'Criteriosaspectos', 'db_table': "u'criteriosaspectos'"},
            'aspectos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Aspectos']"}),
            'calificacion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '2', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '2', 'blank': 'True'})
        },
        u'principal.criteriosjurado': {
            'Meta': {'object_name': 'Criteriosjurado', 'db_table': "u'criteriosjurado'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.cronogramas': {
            'Meta': {'object_name': 'Cronogramas', 'db_table': "u'cronogramas'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'fechafin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fechainicio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.docentes': {
            'Meta': {'object_name': 'Docentes', 'db_table': "u'docentes'"},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dni': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tipodocente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Tipodocente']"})
        },
        u'principal.docentesconsejocurricular': {
            'Meta': {'object_name': 'DocentesConsejocurricular', 'db_table': "u'docentes_consejocurricular'"},
            'concejocurricular': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Concejocurricular']"}),
            'docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_dni'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.documentacion': {
            'Meta': {'object_name': 'Documentacion', 'db_table': "u'documentacion'"},
            'asunto': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'documentacion_alterna': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Documentacion']", 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.empresaspasantes': {
            'Meta': {'object_name': 'Empresaspasantes', 'db_table': "u'empresaspasantes'"},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nit': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tiposempresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Tiposempresa']"})
        },
        u'principal.estudiantes': {
            'Meta': {'object_name': 'Estudiantes', 'db_table': "u'estudiantes'"},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dni': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.evaluacionestrabajogrado': {
            'Meta': {'object_name': 'Evaluacionestrabajogrado', 'db_table': "u'evaluacionestrabajogrado'"},
            'caracter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Caracter']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'nota_final_aspectos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'Trabajosgrado_codigo'"})
        },
        u'principal.historicocriteriospropuestas': {
            'Meta': {'object_name': 'Historicocriteriospropuestas', 'db_table': "u'historicocriteriospropuestas'"},
            'concejocurricular': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Concejocurricular']"}),
            'criterios': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Criterios']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'proptg_revt_revtec': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'proptg_revt_revtec'", 'to': u"orm['principal.PropuestatgRevisorest']"}),
            'proptg_revtproptg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.PropuestatgRevisorest']"})
        },
        u'principal.informefinalcriterios': {
            'Meta': {'object_name': 'InformefinalCriterios', 'db_table': "u'informefinal_criterios'"},
            'criteriosjurado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Criteriosjurado']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informesfinales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Informesfinales']"}),
            'jurados_docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'jurados_docentes_dni'", 'db_column': "u'jurados_docentes_dni'", 'to': u"orm['principal.Jurados']"}),
            'jurados_trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Jurados']", 'db_column': "u'jurados_trabajosgrado_codigo'"}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'principal.informesfinales': {
            'Meta': {'object_name': 'Informesfinales', 'db_table': "u'informesfinales'"},
            'concejocurricular': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Concejocurricular']"}),
            'coordinadorestg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Coordinadorestg']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'unique': 'True', 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.informesperiodicos': {
            'Meta': {'object_name': 'Informesperiodicos', 'db_table': "u'informesperiodicos'"},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pasantias_trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Pasantias']", 'db_column': "u'pasantias_trabajosgrado_codigo'"})
        },
        u'principal.jurados': {
            'Meta': {'object_name': 'Jurados', 'db_table': "u'jurados'"},
            'concejocurricular': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Concejocurricular']"}),
            'docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_dni'"}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'presidente': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.modalidadespasantia': {
            'Meta': {'object_name': 'Modalidadespasantia', 'db_table': "u'modalidadespasantia'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.modalidadestg': {
            'Meta': {'object_name': 'Modalidadestg', 'db_table': "u'modalidadestg'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'trabajogrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajogrado_codigo'"})
        },
        u'principal.pasantias': {
            'Meta': {'object_name': 'Pasantias', 'db_table': "u'pasantias'"},
            'codigo': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'empresaspasantes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Empresaspasantes']"}),
            'modalidadespasantia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Modalidadespasantia']"}),
            'propuestaspasantias_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'unique': 'True', 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.propuestatg': {
            'Meta': {'object_name': 'Propuestatg', 'db_table': "u'propuestatg'"},
            'coordinadorestg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Coordinadorestg']"}),
            'fechapresentacion': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.propuestatgrevisorest': {
            'Meta': {'object_name': 'PropuestatgRevisorest', 'db_table': "u'propuestatg_revisorest'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'propuestatg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Propuestatg']"}),
            'revisorestecnicos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Revisorestecnicos']"})
        },
        u'principal.revisorestecnicos': {
            'Meta': {'object_name': 'Revisorestecnicos', 'db_table': "u'revisorestecnicos'"},
            'concepto': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_dni'"}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.solicitudespasantes': {
            'Meta': {'object_name': 'Solicitudespasantes', 'db_table': "u'solicitudespasantes'"},
            'concejocurricular': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Concejocurricular']"}),
            'conceptossolicitudes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Conceptossolicitudes']"}),
            'empresaspasantes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Empresaspasantes']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'revisorestecnicos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Revisorestecnicos']", 'null': 'True', 'blank': 'True'})
        },
        u'principal.supervisoresempresas': {
            'Meta': {'object_name': 'Supervisoresempresas', 'db_table': "u'supervisoresempresas'"},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'dni': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'empresaspasantes_nit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Empresaspasantes']", 'db_column': "u'empresaspasantes_nit'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'principal.sustentaciones': {
            'Meta': {'object_name': 'Sustentaciones', 'db_table': "u'sustentaciones'"},
            'fechapublicacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecharealizacion': ('django.db.models.fields.DateField', [], {}),
            'hora': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nota': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '2', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'unique': 'True', 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.tipodocente': {
            'Meta': {'object_name': 'Tipodocente', 'db_table': "u'tipodocente'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'principal.tiposempresa': {
            'Meta': {'object_name': 'Tiposempresa', 'db_table': "u'tiposempresa'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.trabajosgrado': {
            'Meta': {'object_name': 'Trabajosgrado', 'db_table': "u'trabajosgrado'"},
            'codigo': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'docentes_director': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_director'"}),
            'grupo_investigacion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'nota_definitiva': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '2', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'principal.visitas': {
            'Meta': {'object_name': 'Visitas', 'db_table': "u'visitas'"},
            'coordinadorestg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Coordinadorestg']"}),
            'empresaspasantes_nit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Empresaspasantes']", 'db_column': "u'empresaspasantes_nit'"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'hora': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['principal']