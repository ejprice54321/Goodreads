##################
# This crawler scrapes the first n pages of a book list from Goodreads,
# and stores them as books with titles, authors, and links.
#################

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
from book import Book

def getTitle(bsObj):
    fullList = bsObj.findAll("span", {"itemprop":"name"})
    titleList = []
    for title in fullList[::2]:
        titleList.append(title.get_text())
    return titleList

def getAuthor(bsObj):
    fullList = bsObj.findAll("span", {"itemprop":"name"})
    authorList = []
    for author in fullList[1::2]:
        authorList.append(author.get_text())
    return authorList

def getLink(bsobj):
    table = bsObj.find("table", {"class":"tableList"})
    book = table.findAll("tr")
    linkList =[]
    for tr in book:
        cols = tr.findAll("td")
        link = cols[1].find("a").get("href")
        linkList.append(link)
    return linkList


if __name__ == "__main__":
    url = "https://www.goodreads.com/list/show/1381.Best_Series?page="
    bookObjectList = []
    for i in range(0, 2):
        try:
            html = urlopen(url+str(i))
        except HTTPError as e:
            print(e)
        except URLError as e:
            print("The server could not be found!")
        else:
            print("Scraping page: "+str(i)+" of Best Series book list")
            bsObj = BeautifulSoup(html, "html.parser")
            authorList = getAuthor(bsObj)
            titleList = getTitle(bsObj)
            linkList = getLink(bsObj)
            for i in range(len(linkList)):
                book = Book(titleList[i], authorList[i], linkList[i])
                bookObjectList.append(book)
                print(bookObjectList[i].url)