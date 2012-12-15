# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ArticleTerm'
        db.create_table('blog_articleterm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('blog', ['ArticleTerm'])

        # Adding model 'Article'
        db.create_table('blog_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('blog', ['Article'])

        # Adding M2M table for field terms on 'Article'
        db.create_table('blog_article_terms', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm['blog.article'], null=False)),
            ('articleterm', models.ForeignKey(orm['blog.articleterm'], null=False))
        ))
        db.create_unique('blog_article_terms', ['article_id', 'articleterm_id'])


    def backwards(self, orm):
        # Deleting model 'ArticleTerm'
        db.delete_table('blog_articleterm')

        # Deleting model 'Article'
        db.delete_table('blog_article')

        # Removing M2M table for field terms on 'Article'
        db.delete_table('blog_article_terms')


    models = {
        'blog.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'terms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.ArticleTerm']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'blog.articleterm': {
            'Meta': {'object_name': 'ArticleTerm'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']