from WebScraping.MilestoneProject4.locators.book_locator import BookLocator

class BookParser:


    RATINGS={
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5,
    }


    def __init__(self,parent):
        self.parent = parent

    def __repr__(self):
        return f"<Book {self.name} has rating of :{self.rating} and price of: {self.price} and here is the link {self.link}"

    @property
    def name(self):
        locator = 'article.product_pod h3 a'  ## CSS locator
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def price(self):
        locator =  BookLocator.PRICE
        item_data = self.parent.select_one(locator).string
        item_price_float = float(item_data.replace('£', ''))
        print(item_price_float)
        return item_price_float

    @property
    def rating(self):
        locator = BookLocator.RATING
        star_rating =  self.parent.select_one(locator)
        classes = star_rating.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating = BookParser.RATINGS[rating_classes[0]]
        return rating

    @property
    def link(self):
        locator = BookLocator.LINK
        return self.parent.select_one(locator).attrs['href']