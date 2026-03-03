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



soup  = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_item_name():
    locator = 'article.product_pod h3 a' ## CSS locator
    item_link = soup.select_one(locator)
    item_name = item_link.attrs['title']
    item_link_name = item_link.attrs['href']
    print(item_name)
    print(item_link_name)


def find_number():
    locator = 'article.product_pod p.price_color'
    item = soup.select_one(locator).string
    item_price_float = float(item.replace('$',''))
    print(item_price_float)


    ## With RegEx
    print(f'item ======= {item}')
    pattern = "£([0-9]+\.[0-9]+)"
    matcher = re.search(pattern, item)
    print(matcher)
    print(matcher.group(0))
    print(float(matcher.group(1)))

def find_item_rating():
    locator = 'article.product_pod p.star-rating'
    star_rating = soup.select_one(locator)
    classes = star_rating.attrs['class']
    rating_classes = [r for r in classes if r != 'star-rating']
    # rating_classes = [lambda x: x != 'star-rating',classes]
    print(rating_classes)



find_item_name()
find_number()
find_item_rating()