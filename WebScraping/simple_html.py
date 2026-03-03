from bs4 import BeautifulSoup


SIMPLE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head></head>
<h1>This is simple title</h1>
<p class="subtitle">Another program</p>
<p>Another title program</p>
<ul>
    <li>Home</li>
    <li>Movie</li>
    <li>Pool</li>
    <li>Games</li>
</ul>
</body>
</html> 
"""

simple_soup= BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_title():
    print(simple_soup.find('h1'))
    print(simple_soup.find('h1').string)  # get text without tags

def find_items():
    list_items= simple_soup.find_all('li')

    for item in list_items:
        print(item.string)

def find_subtitle():
    print(simple_soup.find('p',{'class':'subtitle'}).string)

def find_other_para():
    doc = simple_soup.find_all('p')
    print(doc)
    other_para = [p for p in doc if 'subtitle' not in p.attrs.get('class',[])]
    print(other_para[0])

find_title()
find_items()
find_subtitle()
find_other_para()


