from django.db.models.signals import post_save, post_delete 
from django.dispatch import receiver
from .models import Article, ArticleStats
from django.core.cache import cache

@receiver([post_save, post_delete], sender=Article)
def invalidate_article_cache(sender, instance, **kwargs):
    
    cache.delete_pattern('*article_list*')
    print('Кэш очищен для статей')


@receiver([post_save, post_delete], sender=ArticleStats)
def invalidate_statistic_cache(sender, instance, **kwargs):
    
    cache.delete_pattern('*stat_page_data*')
    print('Кэш очищен для статистики')
