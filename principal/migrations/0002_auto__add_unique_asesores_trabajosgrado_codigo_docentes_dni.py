# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Asesores', fields ['trabajosgrado_codigo', 'docentes_dni']
        db.create_unique(u'asesores', [u'trabajosgrado_codigo', u'docentes_dni'])


    def backwards(self, orm):
        # Removing unique constraint on 'Asesores', fields ['trabajosgrado_codigo', 'docentes_dni']
        db.delete_unique(u'asesores', [u'trabajosgrado_codigo', u'docentes_dni'])


    models = {
        u'principal.asesores': {
            'Meta': {'unique_together': "((u'trabajosgrado_codigo', u'docentes_dni'),)", 'object_name': 'Asesores', 'db_table': "u'asesores'"},
            'docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_dni'"}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.aspectos': {
            'Meta': {'object_name': 'Aspectos', 'db_table': "u'aspectos'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'evaluacionestrabajogrado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Evaluacionestrabajogrado']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'porcentaje': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '2'})
        },
        u'principal.caracter': {
            'Meta': {'object_name': 'Caracter', 'db_table': "u'caracter'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.concejocurricular': {
            'Meta': {'object_name': 'Concejocurricular', 'db_table': "u'concejocurricular'", 'managed': 'False'},
            'fechacreacion': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.conceptossolicitudes': {
            'Meta': {'object_name': 'Conceptossolicitudes', 'db_table': "u'conceptossolicitudes'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.conveniomarco': {
            'Meta': {'object_name': 'Conveniomarco', 'db_table': "u'conveniomarco'", 'managed': 'False'},
            'activo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'empresaspasantes_nit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Empresaspasantes']", 'db_column': "u'empresaspasantes_nit'"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.convocatorias': {
            'Meta': {'object_name': 'Convocatorias', 'db_table': "u'convocatorias'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'fechainicio': ('django.db.models.fields.DateField', [], {}),
            'fechalimite': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'solicitudespasantes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Solicitudespasantes']"})
        },
        u'principal.coordinadorestg': {
            'Meta': {'object_name': 'Coordinadorestg', 'db_table': "u'coordinadorestg'", 'managed': 'False'},
            'anio': ('django.db.models.fields.BigIntegerField', [], {'db_column': "u'a\\xf1o'"}),
            'docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_dni'"}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'semestreacademico': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'principal.criterios': {
            'Meta': {'object_name': 'Criterios', 'db_table': "u'criterios'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.criteriosaspectos': {
            'Meta': {'object_name': 'Criteriosaspectos', 'db_table': "u'criteriosaspectos'", 'managed': 'False'},
            'aspectos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Aspectos']"}),
            'calificacion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '2', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'porcentaje': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '2', 'blank': 'True'})
        },
        u'principal.criteriosjurado': {
            'Meta': {'object_name': 'Criteriosjurado', 'db_table': "u'criteriosjurado'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.cronogramas': {
            'Meta': {'object_name': 'Cronogramas', 'db_table': "u'cronogramas'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'fechafin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fechainicio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.docentes': {
            'Meta': {'object_name': 'Docentes', 'db_table': "u'docentes'", 'managed': 'False'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dni': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tipodocente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Tipodocente']"})
        },
        u'principal.docentesconsejocurricular': {
            'Meta': {'object_name': 'DocentesConsejocurricular', 'db_table': "u'docentes_consejocurricular'", 'managed': 'False'},
            'concejocurricular': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Concejocurricular']"}),
            'docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_dni'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.documentacion': {
            'Meta': {'object_name': 'Documentacion', 'db_table': "u'documentacion'", 'managed': 'False'},
            'asunto': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'documentacion_alterna': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Documentacion']", 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.empresaspasantes': {
            'Meta': {'object_name': 'Empresaspasantes', 'db_table': "u'empresaspasantes'", 'managed': 'False'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nit': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tiposempresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Tiposempresa']"})
        },
        u'principal.estudiantes': {
            'Meta': {'object_name': 'Estudiantes', 'db_table': "u'estudiantes'", 'managed': 'False'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dni': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.evaluacionestrabajogrado': {
            'Meta': {'object_name': 'Evaluacionestrabajogrado', 'db_table': "u'evaluacionestrabajogrado'", 'managed': 'False'},
            'caracter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Caracter']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'nota_final_aspectos': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'Trabajosgrado_codigo'"})
        },
        u'principal.historicocriteriospropuestas': {
            'Meta': {'object_name': 'Historicocriteriospropuestas', 'db_table': "u'historicocriteriospropuestas'", 'managed': 'False'},
            'concejocurricular': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Concejocurricular']"}),
            'criterios': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Criterios']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'proptg_revt_revtec': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'proptg_revt_revtec'", 'to': u"orm['principal.PropuestatgRevisorest']"}),
            'proptg_revtproptg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.PropuestatgRevisorest']"})
        },
        u'principal.informefinalcriterios': {
            'Meta': {'object_name': 'InformefinalCriterios', 'db_table': "u'informefinal_criterios'", 'managed': 'False'},
            'criteriosjurado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Criteriosjurado']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informesfinales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Informesfinales']"}),
            'jurados_docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'jurados_docentes_dni'", 'db_column': "u'jurados_docentes_dni'", 'to': u"orm['principal.Jurados']"}),
            'jurados_trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Jurados']", 'db_column': "u'jurados_trabajosgrado_codigo'"}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'principal.informesfinales': {
            'Meta': {'object_name': 'Informesfinales', 'db_table': "u'informesfinales'", 'managed': 'False'},
            'concejocurricular': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Concejocurricular']"}),
            'coordinadorestg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Coordinadorestg']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'unique': 'True', 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.informesperiodicos': {
            'Meta': {'object_name': 'Informesperiodicos', 'db_table': "u'informesperiodicos'", 'managed': 'False'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pasantias_trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Pasantias']", 'db_column': "u'pasantias_trabajosgrado_codigo'"})
        },
        u'principal.jurados': {
            'Meta': {'object_name': 'Jurados', 'db_table': "u'jurados'", 'managed': 'False'},
            'concejocurricular': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Concejocurricular']"}),
            'docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_dni'"}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'presidente': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.modalidadespasantia': {
            'Meta': {'object_name': 'Modalidadespasantia', 'db_table': "u'modalidadespasantia'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.modalidadestg': {
            'Meta': {'object_name': 'Modalidadestg', 'db_table': "u'modalidadestg'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'trabajogrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajogrado_codigo'"})
        },
        u'principal.pasantias': {
            'Meta': {'object_name': 'Pasantias', 'db_table': "u'pasantias'", 'managed': 'False'},
            'codigo': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'empresaspasantes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Empresaspasantes']"}),
            'modalidadespasantia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Modalidadespasantia']"}),
            'propuestaspasantias_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'unique': 'True', 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.propuestatg': {
            'Meta': {'object_name': 'Propuestatg', 'db_table': "u'propuestatg'", 'managed': 'False'},
            'coordinadorestg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Coordinadorestg']"}),
            'fechapresentacion': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.propuestatgrevisorest': {
            'Meta': {'object_name': 'PropuestatgRevisorest', 'db_table': "u'propuestatg_revisorest'", 'managed': 'False'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'propuestatg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Propuestatg']"}),
            'revisorestecnicos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Revisorestecnicos']"})
        },
        u'principal.revisorestecnicos': {
            'Meta': {'object_name': 'Revisorestecnicos', 'db_table': "u'revisorestecnicos'", 'managed': 'False'},
            'concepto': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'docentes_dni': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_dni'"}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.solicitudespasantes': {
            'Meta': {'object_name': 'Solicitudespasantes', 'db_table': "u'solicitudespasantes'", 'managed': 'False'},
            'concejocurricular': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Concejocurricular']"}),
            'conceptossolicitudes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Conceptossolicitudes']"}),
            'empresaspasantes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Empresaspasantes']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'revisorestecnicos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Revisorestecnicos']", 'null': 'True', 'blank': 'True'})
        },
        u'principal.supervisoresempresas': {
            'Meta': {'object_name': 'Supervisoresempresas', 'db_table': "u'supervisoresempresas'", 'managed': 'False'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'dni': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'empresaspasantes_nit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Empresaspasantes']", 'db_column': "u'empresaspasantes_nit'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'principal.sustentaciones': {
            'Meta': {'object_name': 'Sustentaciones', 'db_table': "u'sustentaciones'", 'managed': 'False'},
            'fechapublicacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecharealizacion': ('django.db.models.fields.DateField', [], {}),
            'hora': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nota': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '2', 'blank': 'True'}),
            'trabajosgrado_codigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Trabajosgrado']", 'unique': 'True', 'db_column': "u'trabajosgrado_codigo'"})
        },
        u'principal.tipodocente': {
            'Meta': {'object_name': 'Tipodocente', 'db_table': "u'tipodocente'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'principal.tiposempresa': {
            'Meta': {'object_name': 'Tiposempresa', 'db_table': "u'tiposempresa'", 'managed': 'False'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        u'principal.trabajosgrado': {
            'Meta': {'object_name': 'Trabajosgrado', 'db_table': "u'trabajosgrado'", 'managed': 'False'},
            'codigo': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'docentes_director': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Docentes']", 'db_column': "u'docentes_director'"}),
            'grupo_investigacion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'nota_definitiva': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '2', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'principal.visitas': {
            'Meta': {'object_name': 'Visitas', 'db_table': "u'visitas'", 'managed': 'False'},
            'coordinadorestg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Coordinadorestg']"}),
            'empresaspasantes_nit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Empresaspasantes']", 'db_column': "u'empresaspasantes_nit'"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'hora': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['principal']