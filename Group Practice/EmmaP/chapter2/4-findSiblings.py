from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.goodreads.com/search?utf8=%E2%9C%93&query=book")
bsObj = BeautifulSoup(html, "html.parser")

for sibling in bsObj.find("table",{"class":"tableList"}).tr.next_siblings:
    print(sibling) 