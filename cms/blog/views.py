from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Article


def index(request):
  article_list = Article.objects.filter(published=True).order_by('-pub_date')[:5]
  return render_to_response('blog/index.html', {'article_list': article_list})

def article(request, slug, article_id):
  article = get_object_or_404(Article, pk=article_id)
  return render_to_response('blog/article.html', {'article': article})
