from django.db import models

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
