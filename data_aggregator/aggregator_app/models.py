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

    def __str__(self):
        return self.title