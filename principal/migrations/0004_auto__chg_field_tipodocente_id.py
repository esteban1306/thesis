# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tipodocente.id'
        db.alter_column(u'tipodocente', 'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

    def backwards(self, orm):

        # Changing field 'Tipodocente.id'
        db.alter_column(u'tipodocente', 'id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))

    models = {
        u'principal.asesores': {
            'Meta': {'unique_together': "((u'trabajosgrado_codigo', u'docentes_dni'),)", 'object_name': 'Asesores', 'db_table': "u'asesores'"},
            'docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_dni'"}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.aspectos': {
            'Meta': {'object_name': 'Aspectos', 'db_table': "u'aspectos'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'evaluacionestrabajogrado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Evaluacionestrabajogrado']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'porcentaje': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
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
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'calificacion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'})
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
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'principal.documentacion': {
            'Meta': {'object_name': 'Documentacion', 'db_table': "u'documentacion'"},
            'asunto': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'documentacion': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'documentacion_alterna'", 'null': 'True', 'to': u"orm['principal.Documentacion']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nota_final_aspectos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'Trabajosgrado_codigo'"})
        },
        u'principal.historicocriteriospropuestas': {
            'Meta': {'object_name': 'Historicocriteriospropuestas', 'db_table': "u'historicocriteriospropuestas'"},
            'concejocurricular': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Concejocurricular']"}),
            'criterios': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Criterios']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'propuestatg_revisorest': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.PropuestatgRevisorest']"})
        },
        u'principal.informefinalcriterios': {
            'Meta': {'object_name': 'InformefinalCriterios', 'db_table': "u'informefinal_criterios'"},
            'criteriosjurado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Criteriosjurado']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'informesfinales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Informesfinales']"}),
            'jurados': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Jurados']"}),
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
            'Meta': {'unique_together': "((u'trabajosgrado_codigo', u'docentes_dni'),)", 'object_name': 'Jurados', 'db_table': "u'jurados'"},
            'concejocurricular': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Concejocurricular']"}),
            'docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_dni'"}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
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
            'Meta': {'unique_together': "((u'propuestatg', u'revisorestecnicos'),)", 'object_name': 'PropuestatgRevisorest', 'db_table': "u'propuestatg_revisorest'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
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
            'nota': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'unique': 'True', 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.tipodocente': {
            'Meta': {'object_name': 'Tipodocente', 'db_table': "u'tipodocente'"},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'modalidadestg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Modalidadestg']"}),
            'nota_definitiva': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
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