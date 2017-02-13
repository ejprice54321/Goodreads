from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from urllib.error import HTTPError
from urllib.error import URLError


url = "https://www.goodreads.com/book/show/256683.City_of_Bones"
# bsObj = BeautifulSoup(html, "html.parser")
# table = bsObj.find("div", {"id":"bookReviews"})
# rating = (bsObj.find("span",{"class":"average"})).get_text()
# cost = (bsObj.find("li", {"class":"firstBuyButton"})).get_text()
# for row in table.findAll("div", {"class": "review"}):

# 	reviewer = (row.find("a", {"class":"user"})).get_text()
# 	rating = (row.find("span", {"size":"15x15"})).get_text()
# 	content = (row.find("div", {"class":"reviewText stacked"})).get_text()
# 	likes = (row.find("span", {"class":"likesCount"})).get_text()
# 	date = (row.find("a", {"class":"reviewDate createdAt right"})).get_text()
# 	# if title == "Literary Awards":
# 	# 	print(title, info)
# 	# elif title == "Characters":
# 	# 	print(title, info)
# 	print(reviewer, rating, content, likes, date)
# print(cost)


# reviewer = (bsObj.find("a", {"class":"user"})).get_text()

# def getLinks(bsObj):
#     table = bsObj.find("table", {"class":"tableList"})
#     book = table.findAll("tr")
#     linkList =[]
#     for tr in book:
#         cols = tr.findAll("td")
#         link = cols[1].find("a").get("href")
#         linkList.append(link)
#     return linkList

link = urlopen("https://www.goodreads.com/book/show/2623.Great_Expectations")
bsObj = BeautifulSoup(link, "html.parser")
try:
	publication = bsObj.find("nobr",{"class":"greyText"}).get_text()
except:
	greyText = bsObj.findAll("div",{"class":"row"})
	publication = greyText[1].get_text()
print(publication)

# name = authorPage.find('h1').get_text()
# birth = authorPage.find("div",{"itemprop":"birthDate"}).get_text()
# death = authorPage.find("div",{"itemprop":"deathDate"}).get_text()
# website = authorPage.find("a",{"itemprop":"url"}).get("href")
# bio = authorPage.find("div",{"class":"aboutAuthorInfo"}).get_text()

# table = bsObj.find("div", {"class":"rightContainer"})
# for row in table.findAll("div", {"class":"clearFloats"}):
#     info = (row.find("div", {"class":"infoBoxRowTitle"})).get_text()
#     item = (row.find("div", {"class":"infoBoxRowItem"})).get_text()
#     if info == "Characters":
#         characters = item
#     elif info == "Literary Awards":
#         awards = item

# print (name,birth,death,website,bio)


# url = "https://www.goodreads.com/"
# fullList = []

# for i in range(174):
# 	pageCrawler = crawl(url + "list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page=" + str(i))
# 	fullList = getLinks(pageCrawler)
# 	print(fullList)

