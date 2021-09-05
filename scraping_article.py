import requests
from bs4 import BeautifulSoup


url = 'https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html?action=click&module=Opinion&pgtype=Homepage'
source = requests.get(url)

soup = BeautifulSoup(source.content, 'html.parser')


def article_title():
    print(soup.title.text, end='\n'*2)

def author():
    author = soup.find('a', class_='css-ozn3l9 e1jsehar0')
    print(author.text, end='\n'*2)
def paragraphs():
    ps = soup.find_all('p', class_='css-axufdj evys1bk0')
    for p in ps:
        print(p.text)
        print()
article_title(), author(), paragraphs()
