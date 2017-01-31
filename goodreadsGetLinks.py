from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj	=	BeautifulSoup(html)
for	link	in	bsObj.findAll("a"):
				if	'href'	in	link.attrs:
								print(link.attrs['href'])