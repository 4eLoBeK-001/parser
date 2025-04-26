from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Article(models.Model):
    class SourceChoice(models.TextChoices):
        HABR = 'Habr'
        VC = 'Vc'
    
    title = models.CharField(max_length=255)
    url = models.URLField(help_text='Ссылка на источник')
    source = models.CharField(choices=SourceChoice, help_text='Источник')
    publication_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0, help_text='Положительный голос')
    downvotes = models.IntegerField(default=0, help_text='Отрицательный голос')

    class Meta:
        ordering = ('-publication_date',)

    @property
    def rating(self):
        return self.upvotes + self.downvotes

    def __str__(self):
        return self.title
    
    def upvote(self):
        self.upvotes += 1
        self.save()

    def downvote(self):
        self.downvotes -= 1
        self.save()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=120)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий от {self.author_name} на {self.article.title}'


class ArticleStats(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='statistic')
    views = models.IntegerField(default=0)
    unique_visitors = models.JSONField(default=list, help_text='Список уникальных поситителей')

    # Для уникальных посетителей
    def add_view(self, request):
        self.views += 1
        # Если пользователь авторизован, то уникальный визит зависит от его его id.
        # Если пользователь анонимный, то уникальный визит зависит от его ip адреса.
        visitor = request.user.id if request.user.is_authenticated else request.META.get('REMOTE_ADDR')
        
        if visitor not in self.unique_visitors:
            self.unique_visitors.append(visitor)

        self.save()


class Vote(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL)
    ip_address = models.CharField(max_length=45)
    vote_type = models.SmallIntegerField(choices=((1, 'Upvote'), (-1, 'Downvote')))
    created_at = models.DateTimeField(auto_now_add=True)
