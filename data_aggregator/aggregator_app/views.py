from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CreateCommentForm
from .models import Article, ArticleStats, Vote
# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'source': Article.SourceChoice.HABR
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

def article_stats(request):
    articles = Article.objects.all()
    top_views_articles = articles.order_by('-statistic__views')[:5]
    top_rating_articles = articles.order_by('-upvotes')[:5]

    context = {
        'total_articles': articles.count(),

        'most_viewed': top_views_articles.first(),
        'top_views_articles': top_views_articles,

        'top_rating_articles': top_rating_articles,
        'heading': 'Статистика'
    }
    return render(request, 'aggregator_app/stats.html', context)


def article_upvote(request, article_id):
    _handle_vote(request, article_id, 1)
    
    return redirect(request.META.get('HTTP_REFERER'))

def article_downvote(request, article_id):
    _handle_vote(request, article_id, -1)
    
    return redirect(request.META.get('HTTP_REFERER'))


def _handle_vote(request, article_id, vote_type):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    ip = request.META.get('REMOTE_ADDR')

    vote = Vote.objects.filter(Q(article=article) & (Q(user=user) | Q(ip_address=ip))).exists()
    
    if vote:
        raise PermissionDenied('Вы уже голосовали за эту статью')
    else:
        Vote.objects.create(
            article=article, 
            user=user if user.is_authenticated else None,
            ip_address=ip,
            vote_type=vote_type
        )
    
    if vote_type==1:
        article.upvote()
    else:
        article.downvote()
