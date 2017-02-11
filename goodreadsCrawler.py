##################
# This crawler scrapes the first n pages of a book list from Goodreads,
# and stores them as books with titles, authors, and links.
#################

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
from database import Database
from book import Book
import pymysql

class Crawler:	

    #########
    # Grabs the title of the book.
    #########
    def getTitle(self, bsObj):
        fullList = bsObj.findAll("h1", {"itemprop":"name"})
        return fullList

    #########
    # Grabs the author of the book.
    #########
    def getAuthor(self, bsObj):
        fullList = bsObj.findAll("span", {"itemprop":"name"})
        return fullList

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
            listObj = BeautifulSoup(html, "html.parser")
            return listObj


    ################
    # Searches a given Goodreads book page and records its description, rating, characters, setting, and awards.
    ##############
    def searchBook(self, bsObj):
        bookList = []
        titleList = self.getTitle(bsObj)
        authorList = self.getAuthor(bsObj)
        print (titleList, authorList)

if __name__ == "__main__":
    db = Database()
    url = "https://www.goodreads.com/"
    crawler = Crawler()
    bsObj = crawler.crawl(url + "list/show/1381.Best_Series?page=")
    linkList = crawler.getLinks(bsObj)
    print(linkList)
    books = {};
    for i in range(len(linkList)):
        bsObj = crawler.crawl(url + str(linkList[i]))
        crawler.searchBook(bsObj)