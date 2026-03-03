from importlib.metadata import requires
from sys import executable

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests

from WebScraping.Scraping_quotes.pages.quotes_page import QuotePage

# page_content = requests.get("https://quotes.toscrape.com/").content
# page =  QuotePage(page_content)


service =Service(executable_path=r"C:\Users\lcom\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
chrome = webdriver.Chrome(service=service)
chrome.get("https://quotes.toscrape.com/")
page = QuotePage(chrome)



for quote in page.quotes:
    print(quote)
    print(quote.content)


