from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.goodreads.com/search?utf8=%E2%9C%93&query=book")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.find("img",{"src" : "https://images.gr-assets.com/books/1390053681s/19063.jpg"}).parent.previous_sibling.get_text())
