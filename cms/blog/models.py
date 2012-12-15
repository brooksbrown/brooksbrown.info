from django.db import models
from django.contrib import admin

# Create your models here.


class ArticleTerm(models.Model):
  title = models.CharField(max_length=100)

  def __unicode__(self):
    return self.title




class Article(models.Model):
  title = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  body = models.TextField()
  terms = models.ManyToManyField(ArticleTerm)
  published = models.BooleanField()
 
  def __unicode__(self):
    return self.title



#admin calls
class ArticleAdmin(admin.ModelAdmin):
      pass
class ArticleTermAdmin(admin.ModelAdmin):
    pass

admin.site.register(ArticleTerm, ArticleTermAdmin)
admin.site.register(Article, ArticleAdmin)
