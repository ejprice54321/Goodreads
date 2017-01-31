from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.goodreads.com/search?utf8=%E2%9C%93&query=book")
bsObj = BeautifulSoup(html, "lxml")
for	link in bsObj.find("div", {"class":"leftContainer"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
	if 'href' in link.attrs:
		print(link.attrs['href'])