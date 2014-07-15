# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table(u'course_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('courseCode', self.gf('django.db.models.fields.CharField')(default='No code yet', max_length=25)),
            ('title', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('start', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('end', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'course', ['Course'])

        # Adding model 'Lecture'
        db.create_table(u'course_lecture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course.Course'])),
            ('lectureCode', self.gf('django.db.models.fields.CharField')(default='No code yet', max_length=25)),
            ('weekNumber', self.gf('django.db.models.fields.IntegerField')(default='No week number assigned')),
        ))
        db.send_create_signal(u'course', ['Lecture'])

        # Adding model 'Content'
        db.create_table(u'course_content', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course.Lecture'])),
            ('contentCode', self.gf('django.db.models.fields.CharField')(default='No code yet', max_length=25)),
            ('title', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'course', ['Content'])

        # Adding model 'Assignment'
        db.create_table(u'course_assignment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course.Course'])),
            ('assignmentCode', self.gf('django.db.models.fields.CharField')(default='No code yet', max_length=25)),
            ('postedDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('dueDate', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('title', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('maxGrade', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('status', self.gf('django.db.models.fields.CharField')(default='active', max_length=25)),
        ))
        db.send_create_signal(u'course', ['Assignment'])


    def backwards(self, orm):
        # Deleting model 'Course'
        db.delete_table(u'course_course')

        # Deleting model 'Lecture'
        db.delete_table(u'course_lecture')

        # Deleting model 'Content'
        db.delete_table(u'course_content')

        # Deleting model 'Assignment'
        db.delete_table(u'course_assignment')


    models = {
        u'course.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'assignmentCode': ('django.db.models.fields.CharField', [], {'default': "'No code yet'", 'max_length': '25'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['course.Course']"}),
            'dueDate': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxGrade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'postedDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '25'}),
            'title': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'course.content': {
            'Meta': {'object_name': 'Content'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contentCode': ('django.db.models.fields.CharField', [], {'default': "'No code yet'", 'max_length': '25'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['course.Lecture']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'course.course': {
            'Meta': {'object_name': 'Course'},
            'courseCode': ('django.db.models.fields.CharField', [], {'default': "'No code yet'", 'max_length': '25'}),
            'end': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'course.lecture': {
            'Meta': {'object_name': 'Lecture'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['course.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lectureCode': ('django.db.models.fields.CharField', [], {'default': "'No code yet'", 'max_length': '25'}),
            'weekNumber': ('django.db.models.fields.IntegerField', [], {'default': "'No week number assigned'"})
        }
    }

    complete_apps = ['course']