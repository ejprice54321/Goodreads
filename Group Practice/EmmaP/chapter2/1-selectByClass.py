from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.goodreads.com/search?utf8=%E2%9C%93&query=book")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("span", {"itemprop":"name"})
for name in nameList:
    print(name.get_text())