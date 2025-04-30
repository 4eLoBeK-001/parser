from .models import Article

def number_of_news_processor(request):
    return {
        'news_count': Article.objects.all().count()
    }