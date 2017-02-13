##################
# This crawler scrapes the first n pages of a book list from Goodreads,
# and stores them as books with titles, authors, and links.
#################

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
from book import Book
from review import Review
from author import Author
import pymysql

class Goodreads:

    #########
    # Grabs the information from a book.
    #########
    def getReview(self,bsObj, bookTitle):
        book = bookTitle
        reviewer = (bsObj.find("a", {"class":"user"})).get_text()
        content = (bsObj.find("div", {"class":"reviewText stacked"})).get_text()
        try:
            likes = (bsObj.find("span", {"class":"likesCount"})).get_text()
        except:
            likes = 0
        date = (bsObj.find("a", {"class":"reviewDate createdAt right"})).get_text()
        try:
            rating = (bsObj.find("span", {"size":"15x15"})).get_text()
        except:
            rating = 0
        review = Review(book,reviewer,content,likes,date,rating)
        return review


    #########
    # Grabs the information related to the author of a book
    # Returns the author object
    #########
    def getAuthor(self,authorPage):
        name = authorPage.find('h1').get_text()
        try:
            birth = authorPage.find("div",{"itemprop":"birthDate"}).get_text()
        except:
            birth = 0
        try:
            death = authorPage.find("div",{"itemprop":"deathDate"}).get_text()
        except:
            death = 0
        try:
            website = authorPage.find("a",{"itemprop":"url"}).get("href")
        except:
            website = 0
        bio = authorPage.find("div",{"class":"aboutAuthorInfo"}).get_text()
        author = Author(name,birth,death,website,bio)
        print(bio)


    #########
    # Grabs the information related to a book
    # Returns the book object
    #########
    def getBook(self, bsObj):
        awards = 0
        characters = 0
        title = (bsObj.find("h1", {"itemprop":"name"})).get_text()
        author = (bsObj.find("span", {"itemprop":"name"})).get_text()
        description = (bsObj.find("div", {"id":"description"})).get_text()
        try:
            publication = bsObj.find("nobr",{"class":"greyText"}).get_text()
        except:
            greyText = bsObj.findAll("div",{"class":"row"})
            publication = greyText[1].get_text()
        bookType = (bsObj.find("span", {"itemprop":"bookFormatType"})).get_text()
        pages = (bsObj.find("span", {"itemprop":"numberOfPages"})).get_text()
        rating = (bsObj.find("span",{"class":"average"})).get_text()
        table = bsObj.find("div", {"id":"bookDataBox"})
        for row in table.findAll("div", {"class":"clearFloats"}):
            info = (row.find("div", {"class":"infoBoxRowTitle"})).get_text()
            item = (row.find("div", {"class":"infoBoxRowItem"})).get_text()
            if info == "Characters":
                characters = item
            elif info == "Literary Awards":
                awards = item
        reviewTable = bsObj.find("div", {"id":"bookReviews"})
        for row in reviewTable.findAll("div", {"class": "review"}):
            review = self.getReview(row, title)
        self.getAuthorLink(bsObj)
        book = Book(title, author, description, bookType, pages, rating, characters, awards, publication)
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
    # Prints content of books in the bookObjectList when called
    #########
    def printContent(self, bookList):
        print(bookList[i].bookUrl)



    def getAuthorLink(self,bsObj):
        authorURL = bsObj.find("a",{"class":"actionLink moreLink"}).get("href")
        authorObject = self.crawl(url + authorURL)
        author = self.getAuthor(authorObject)


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

if __name__ == "__main__":
    url = "https://www.goodreads.com/"
    goodreads = Goodreads()
    reviewCount = 0
    linkCount = 0
    bookCount = 0
    # bsObj = goodreads.crawl(url + "list/show/1381.Best_Series?page=")
    # linkList = goodreads.getLinks(bsObj)
    fullList = []
    for i in range(5):
        bsObj = goodreads.crawl(url + "list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page=" + str(i))
        linkList = goodreads.getLinks(bsObj)
        for link in range(len(linkList)):
            fullList.append(link)
    print(linkList)
    books = {};
    for i in range(len(linkList)):
        bsObj = goodreads.crawl(url + str(linkList[i]))
        goodreads.searchBook(bsObj)