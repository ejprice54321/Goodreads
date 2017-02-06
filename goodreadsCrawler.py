##################
# This crawler scrapes the first n pages of a book list from Goodreads,
# and stores them as books with titles, authors, and links.
#################

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
from book import Book

class Crawler:

    #########
    # Grabs the title of each book on the page and stores it in a titleList.
    # Returns the titleList.
    #########
    def getTitle(self, bsObj):
        fullList = bsObj.findAll("span", {"itemprop":"name"})
        titleList = []
        for title in fullList[::2]:
            titleList.append(title.get_text())
        return titleList

    #########
    # Grabs the author of each book on the page and stores it in an authorList.
    # Returns the authorList.
    #########
    def getAuthor(self, bsObj):
        fullList = bsObj.findAll("span", {"itemprop":"name"})
        authorList = []
        for author in fullList[1::2]:
            authorList.append(author.get_text())
        return authorList

    #########
    # Grabs the url of each book on the page and stores it in a linkList.
    # Returns the linkList.
    #########
    def getLink(self, bsObj):
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
    def printContent(self, bookObjectList):
        print(bookObjectList[i].bookUrl)

    ################
    # Starts a search of a given Goodreads book list url for a j# of pages,
    # creates a list of book objects and stores the info grabbed in each object.
    # Returns a list of the book objects.
    ##############
    def crawl(self, url):
        bookObjectList = []
        try:
            html = urlopen(url)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print("The server could not be found!")
        else:
            print("Scraping Best Series book list page")
            bsObj = BeautifulSoup(html, "html.parser")
            authorList = self.getAuthor(bsObj)
            titleList = self.getTitle(bsObj)
            linkList = self.getLink(bsObj)
            for i in range(len(linkList)):
                book = Book(titleList[i], authorList[i], linkList[i])
                bookObjectList.append(book)
            return bookObjectList


if __name__ == "__main__":
    url = "https://www.goodreads.com/list/show/1381.Best_Series?page="
    crawler = Crawler()
    bookList = crawler.crawl(url)
    for i in range(len(bookList)):
        crawler.printContent(bookList)
