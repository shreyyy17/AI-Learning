from selenium.webdriver.common.by import By
from WebScraping.Scraping_quotes.locators.quote_page_locator import QuotesPageLocators
from WebScraping.Scraping_quotes.parsers.quote import QuoteParser


class QuotePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        return [
            QuoteParser(e)
            for e in self.browser.find_elements(By.CSS_SELECTOR, locator)
        ]