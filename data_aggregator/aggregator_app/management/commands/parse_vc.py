from django.core.management.base import BaseCommand
from aggregator_app.parser import parse_news_vc

class Command(BaseCommand):
    help = 'Парсинг новостей Vc'

    def handle(self, *args, **options):
        parse_news_vc()
        self.stdout.write(self.style.SUCCESS('Successfully parsed news'))
