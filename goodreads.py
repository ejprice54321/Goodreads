##################
# This crawler scrapes the first n pages of a book list from Goodreads,
# and stores them as books with titles, authors, and links.
#################

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
from book import Book
import pymysql

class Goodreads:

    #########
    # Grabs the title of the book.
    #########
    def getBook(self, bsObj):
        awards = 0
         = 0
        awards = 0
        title = (bsObj.find("h1", {"itemprop":"name"})).get_text()
        author = (bsObj.find("span", {"itemprop":"name"})).get_text()
        description = (bsObj.find("div", {"id":"description"})).get_text()
        bookType = (bsObj.find("span", {"itemprop":"bookFormatType"})).get_text()
        pages = (bsObj.find("span", {"itemprop":"numberOfPages"})).get_text()
        rating = (bsObj.find("span",{"class":"average"})).get_text()
        table = bsObj.find("div", {"id":"bookDataBox"})
        for row in table.findAll("div", {"class":"clearFloats"}):
            title = (row.find("div", {"class":"infoBoxRowTitle"})).get_text()
            item = (row.find("div", {"class":"infoBoxRowItem"})).get_text()
            if title == "Characters":
                characters = item
            elif title == "Literary Awards":
                awards = item
        book = Book(title, author, description, bookType, pages, rating, characters, awards)
        return book
    #########
    # Grabs the url of each book on the page and stores it in a linkList.
    # Returns the linkList.
    #########
    def getLinks(self, bsObj):
        table = bsObj.find("table", {"class":"tableList"})
        book = table.findAll("tr")
        linkList =[]
        for tr in book:
            cols = tr.findAll("td")
            link = cols[1].find("a").get("href")
            linkList.append(link)
        return linkList

    #########
    # Prints content of books in the bookObjectList
    #########
    def printContent(self, bookList):
        print(bookList[i].bookUrl)

    ################
    # Starts a search of a given url.
    # Returns its BeautifulSoup object.
    ##############
    def crawl(self, url):
        try:
            html = urlopen(url)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print("The server could not be found!")
        else:
            print("Scraping new page")
            bsObj = BeautifulSoup(html, "html.parser")
            return bsObj


    ################
    # Searches a given Goodreads book page and records its description, rating, characters, setting, and awards.
    ##############
    def searchBook(self, bsObj):
        book = self.getBook(bsObj)
        print (book.awards)

if __name__ == "__main__":
    url = "https://www.goodreads.com/"
    goodreads = Goodreads()
    bsObj = goodreads.crawl(url + "list/show/1381.Best_Series?page=")
    linkList = goodreads.getLinks(bsObj)
    # print(linkList)
    books = {};
    for i in range(len(linkList)):
        bsObj = goodreads.crawl(url + str(linkList[i]))
        goodreads.searchBook(bsObj)