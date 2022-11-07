import bs4
import requests
import re

# определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'Python']


url = 'https://tproger.ru/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)

text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    headlines = article.find_all(class_='article__link')
    headlines = [head.text.strip() for head in headlines]
    href = article.find(class_='article__link').attrs['href']
    response1 = requests.get(href, headers=headers)
    text1 = response1.text
    soup1 = bs4.BeautifulSoup(text1, features='html.parser')
    articles1 = soup1.find_all('article')
    for article1 in articles1:
        date = article1.find_all(class_='localtime meta__date')
        date = [head.text.strip() for head in date]
        headlines1 = article1.find_all(class_='single__content')
        headlines1 = [head.text.strip() for head in headlines1]
        for word in headlines1:
            for keywords in KEYWORDS:
                if re.search(keywords, word):
                    print()
                    print(f'Ссылка содержит ключевое слово - "{keywords}"')
                    print(f'{date} - {headlines} - {href}')
