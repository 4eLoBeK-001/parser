from django.shortcuts import get_object_or_404, render

from .models import Article
# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'aggregator_app/article_list.html', context)


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        'article': article
    }
    return render(request, 'aggregator_app/article_detail.html', context)

