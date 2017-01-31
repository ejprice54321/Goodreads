from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        titles = bsObj.findAll("span", {"itemprop":"name"})
    except AttributeError as e:
        return None
    return titles

titles = getTitle("https://www.goodreads.com/search?utf8=%E2%9C%93&query=book")
if titles == None:
    print("Title could not be found")
else:
	for i, title in enumerate(titles):
		print(titles[i].get_text())
    
    