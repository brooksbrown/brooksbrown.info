from django.db import models
from django.contrib import admin

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  body = models.TextField()

class ArticleAdmin(admin.ModelAdmin):
      pass


admin.site.register(Article, ArticleAdmin)
