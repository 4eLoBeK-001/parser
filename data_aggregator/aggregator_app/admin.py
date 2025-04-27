from django.contrib import admin

from .models import Article, ArticleStats, Vote
# Register your models here.

admin.site.register(Article)
admin.site.register(ArticleStats)
admin.site.register(Vote)