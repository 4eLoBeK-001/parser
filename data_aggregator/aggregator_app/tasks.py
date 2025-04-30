from celery import shared_task
from datetime import datetime

from .parser import parse_news_habr, parse_news_vc

@shared_task
def parser_periodic_task():
    parse_news_habr()
    parse_news_vc()
    print(f"Задача выполнилась в {datetime.now()}")
    