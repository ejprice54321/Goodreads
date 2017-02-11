from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.goodreads.com/book/show/19063.The_Book_Thief?from_search=true")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("div", {"id":"description"})
print(nameList[0].get_text())