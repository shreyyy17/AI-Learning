import re

from bs4 import BeautifulSoup


SIMPLE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head></head>
<h1>This is simple title</h1>
<p class="subtitle">Another program</p>
<p>Another title program</p>


<article class ="product_pod">
<p class="star-rating Three">
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
</p>
<h3><a href="wgwgwegwe" title="A Light in the Attic">this is title</a></h3>
<p class="price_color">$51.77</p>
</article>
<ul>
    <li>Home</li>
    <li>Movie</li>
    <li>Pool</li>
    <li>Games</li>
</ul>
</body>
</html> 
"""

class ParsedItemLocators:
    """
    Locators for an item in the HTML page

    This allows us to easily see that our code will be looking at
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'




class ParsedItem:
    """
    A class that take in an HTML page (or part of it ) and find properties of an item in it
    """

    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    @property
    def name(self):
        locator = 'article.product_pod h3 a'  ## CSS locator
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = 'article.product_pod h3 a'  ## CSS locator
        item_link = self.soup.select_one(locator).attrs['href']

        return item_link

    @property
    def number(self):
        locator = 'article.product_pod p.price_color'
        item_data = self.soup.select_one(locator).string
        item_price_float = float(item_data.replace('$', ''))
        # return item_price_float

        ## With RegEx
        print(f'item ======= {item}')
        pattern = "$([0-9]+\.[0-9]+)"
        matcher = re.search(pattern, item_data)
        print(matcher)
        print(matcher.group(0))
        print(matcher.group(1))
        return matcher.group(1)


    @property
    def rating(self):
        locator = 'article.product_pod p.star-rating'
        star_rating = self.soup.select_one(locator)
        classes = star_rating.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        # rating_classes = [lambda x: x != 'star-rating',classes]
        return rating_classes[0]




item = ParsedItem(SIMPLE_HTML)
print(item.name)
print(item.link)
print(type(item.number))
print(item.rating)
