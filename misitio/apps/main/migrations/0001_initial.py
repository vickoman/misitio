# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Candidato'
        db.create_table(u'main_candidato', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=144, null=True, blank=True)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=144, null=True, blank=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Candidato'])


    def backwards(self, orm):
        # Deleting model 'Candidato'
        db.delete_table(u'main_candidato')


    models = {
        u'main.candidato': {
            'Meta': {'object_name': 'Candidato'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '144', 'null': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '144', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']