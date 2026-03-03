import requests

from WebScraping.MilestoneProject4.pages.book_page import AllBookPage

page_content = requests.get("https://books.toscrape.com/").content

book_pages = AllBookPage(page_content)
books = book_pages.books


for page_num in range(50):
    url=f"https://books.toscrape.com/catalogue/page/{page_num+1}.html"
    page_content = requests.get(url).content
    page = AllBookPage(page_content)
    books.extend(page.books)
