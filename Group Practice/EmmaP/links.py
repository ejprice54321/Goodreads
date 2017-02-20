from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from urllib.error import HTTPError
from urllib.error import URLError


link = urlopen("https://www.goodreads.com/book/show/29992024-riveted")
bsObj = BeautifulSoup(link, "html.parser")
ratingFrame = bsObj.find("div",{"class":"prototip"})
table = ratingFrame.find("table", {"id":"rating_distribution"})
ratingList = table.get_text()
# for row in table.findAll("tr"):
#     ratingList.append(row.get_text())
print(ratingList)