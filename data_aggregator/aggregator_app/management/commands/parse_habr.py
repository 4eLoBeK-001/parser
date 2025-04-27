from django.core.management.base import BaseCommand
from aggregator_app.parser import parse_news_habr

class Command(BaseCommand):
    help = 'Парсинг новостей Habr'

    def handle(self, *args, **options):
        parse_news_habr()
        self.stdout.write(self.style.SUCCESS('Successfully parsed news'))
