import requests

from bs4 import BeautifulSoup

from .models import Article

def parse_news_habr():
    url = 'https://habr.com/ru/news/'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    items = soup.select('.tm-articles-list__item')[:5]

    for item in items:
        title = item.select_one('.tm-title').text.strip()
        link = item.select_one('a.tm-title__link')['href']
        absolute_link = 'https://habr.com' + link


        if not Article.objects.filter(url=absolute_link).exists():

            Article.objects.create(
                title=title,
                url=absolute_link,
                source=Article.SourceChoice.HABR
            )

def parse_news_vc():

    url = 'https://vc.ru/new'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.select('.content--short')[:5]

    for item in items:
        title = item.select_one('.content-title--low-indent').text.strip()
        link = item.select_one('a.content__link')['href']
        absolute_link = 'https://vc.ru' + link
        
        if not Article.objects.filter(url=absolute_link).exists():
    
            Article.objects.create(
                title=title,
                url=absolute_link,
                source=Article.SourceChoice.VC
            )