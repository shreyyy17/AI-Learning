from bs4 import BeautifulSoup

from WebScraping.MilestoneProject4.locators.book_page_locator import AllBooksPageLocators
from WebScraping.MilestoneProject4.parsers.book_parser import BookParser

class AllBookPage:
    def __init__(self,html):
        self.soup = BeautifulSoup(html, 'html.parser')

    @property
    def books(self):
        locator = AllBooksPageLocators.BOOKS
        all_books = self.soup.select(locator)
        return [BookParser(e) for e in all_books]