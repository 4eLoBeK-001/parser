from django.shortcuts import get_object_or_404, redirect, render

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


def article_upvote(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.upvote()
    
    return redirect(request.META.get('HTTP_REFERER'))

def article_downvote(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.downvote()
    
    return redirect(request.META.get('HTTP_REFERER'))