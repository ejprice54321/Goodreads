from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


html = urlopen("https://www.goodreads.com/book/show/256683.City_of_Bones")
bsObj = BeautifulSoup(html, "html.parser")
table = bsObj.find("div", {"id":"bookDataBox"})
rating = (bsObj.find("span",{"class":"average"})).get_text()
cost = (bsObj.find("li", {"class":"firstBuyButton"})).get_text()
print (cost)

for row in table.findAll("div", {"class": "clearFloats"}):
	title = (row.find("div", {"class":"infoBoxRowTitle"})).get_text()
	info = (row.find("div", {"class":"infoBoxRowItem"})).get_text()	
	if title == "Literary Awards":
		print(title, info)
	elif title == "Characters":
		print(title, info)
# print(cost)