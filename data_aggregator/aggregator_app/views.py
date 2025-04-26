from django.shortcuts import get_object_or_404, redirect, render

from .forms import CreateCommentForm
from .models import Article, ArticleStats
# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'aggregator_app/article_list.html', context)


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    stat, _ = ArticleStats.objects.get_or_create(article=article)
    stat.add_view(request)

    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article=article
            comment.save()
            return redirect(request.META.get('HTTP_REFERER'))
            
    else:
        form = CreateCommentForm()

    context = {
        'article': article,
        'form': form
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