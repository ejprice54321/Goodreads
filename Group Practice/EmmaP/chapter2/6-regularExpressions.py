from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.goodreads.com/search?utf8=%E2%9C%93&query=book")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll("img", {"src":re.compile("\.\.\/image.gr-assets\/books.*\.*\.jpg")})
for image in images: 
    print(image["src"])
