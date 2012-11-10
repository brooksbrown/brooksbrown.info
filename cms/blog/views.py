from django.shortcuts import render_to_response
from blog.models import Article


def index(request):
  article_list = Article.objects.filter(published=True).order_by('-pub_date')[:5]
  return render_to_response('blog/index.html', {'article_list': article_list})
