import requests

from bs4 import BeautifulSoup


# page = requests.get('https://books.toscrape.com/')
page = requests.get('http://www.example.com/')
HTML_CONTENT = page.content


soup = BeautifulSoup(HTML_CONTENT, 'html.parser')

print(soup.find('h1').string)
print(soup.select_one('p a').attrs['href'])