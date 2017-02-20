##################
# This crawler scrapes the first n pages of a book list from Goodreads,
# grabs the links to the books, and from their crawls to the individual
# book and author pages to save information about each in a MySQL database.
#################

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
from book import Book
from review import Review
from author import Author
# from database import Database
import pymysql
import time

class Goodreads:

    #########
    # Grabs the information from a review.
    # Returns the review object.
    #########
    def getReview(self,bsObj, bookTitle):
        book = bookTitle
        try:
            reviewer = (bsObj.find("a", {"class":"user"})).get_text()
        except:
            reviewer = "No reviewer"
        try:
            content = (bsObj.find("div", {"class":"reviewText stacked"})).get_text()
        except:
            content = "No content"
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
        print(review.reviewer)
        # review.save(db)
        return review


    #########
    # Grabs the information from an author's page.
    # Returns the author object.
    #########
    def getAuthor(self, authorPage):
        try:
            name = authorPage.find('h1').get_text()
        except:
            name = "no name"
        try:
            website = authorPage.find("a",{"itemprop":"url"}).get("href")
        except:
            website = 0
        try:
            birth = authorPage.find("div",{"itemprop":"birthDate"}).get_text()
        except:
            birth = 0
        try:
            death = authorPage.find("div",{"itemprop":"deathDate"}).get_text()
        except:
            death = 0
        try:
            bio = authorPage.find("div",{"class":"aboutAuthorInfo"}).get_text()
        except:
            bio = "No bio"
        authorObj = Author(name,website,birth,death,bio)
        print(authorObj.name)
        # authorObj.save(db)
        return authorObj


    #########
    # Grabs the information from a book's page.
    # Returns the book object.
    #########
    def getBook(self, bsObj):
        awards = 0
        characters = 0
        try:
            title = (bsObj.find("h1", {"itemprop":"name"})).get_text()
        except:
            title = 0
        try:
            author = (bsObj.find("span", {"itemprop":"name"})).get_text()
        except:
            author = "No author"
        try:
            description = (bsObj.find("div", {"id":"description"})).get_text()
        except:
            description = 0
        try:
            publication = bsObj.find("nobr",{"class":"greyText"}).get_text()
        except:
            try:
                greyText = bsObj.findAll("div",{"class":"row"})
                publication = greyText[1].get_text()
            except:
                publication = 0
        try:
            bookType = (bsObj.find("span", {"itemprop":"bookFormatType"})).get_text()
        except:
            bookType = "No bookType"
        try:
            pages = (bsObj.find("span", {"itemprop":"numberOfPages"})).get_text()
        except:
            pages = 0
        try:
            rating = (bsObj.find("span",{"class":"average"})).get_text()
        except:
            rating = 0
        try:
            table = bsObj.find("div", {"id":"bookDataBox"})
            for row in table.findAll("div", {"class":"clearFloats"}):
                info = (row.find("div", {"class":"infoBoxRowTitle"})).get_text()
                item = (row.find("div", {"class":"infoBoxRowItem"})).get_text()
                if info == "Characters":
                    characters = item
                elif info == "Literary Awards":
                    awards = item
        except:
            print("NO INFO TABLE")
        try:
            reviewTable = bsObj.find("div", {"id":"bookReviews"})
            for row in reviewTable.findAll("div", {"class": "review"}):
                review = self.getReview(row, title)
        except:
            print("NO REVIEW!!!!!!!!!!")
        self.getAuthorLink(bsObj)
        bookObj = Book(title, author, description, bookType, pages, rating, characters, awards, publication)
        # bookObj.save(db)
        print(bookObj.title)
        return bookObj


    #########
    # Grabs the url of each book on the page and stores it in a linkList.
    # Returns the linkList.
    #########
    def getLinks(self, bsObj, linkList):
        table = bsObj.find("table", {"class":"tableList"})
        book = table.findAll("tr")
        for tr in book:
            cols = tr.findAll("td")
            link = cols[1].find("a").get("href")
            linkList.append(link)
        return linkList

    #########
    # Prints bookUrl of book[i] in the bookObjectList
    #########
    def printContent(self, bookList):
        print(bookList[i].bookUrl)


    #########
    # Grabs the link to the book author's page.
    #########
    def getAuthorLink(self,bsObj):
        try:
            authorURL = bsObj.find("a",{"class":"actionLink moreLink"}).get("href")
            authorObject = self.crawl(url + authorURL)
            author = self.getAuthor(authorObject)
        except:
            print("Couldn't find author page!!!!!!")



    ################
    # Starts a search of a given url.
    # Returns its BeautifulSoup object.
    ##############
    def crawl(self, url):
        try:
            time.sleep(3)
            html = urlopen(url)
        except HTTPError as e:
            print(e)
            return None
        except URLError as e:
            print("The server could not be found!")
            return None
        else:
            print("Scraping new page")
            bsObj = BeautifulSoup(html, "html.parser")
            return bsObj


if __name__ == "__main__":
    url = "https://www.goodreads.com/"
    goodreads = Goodreads()
    # db = Database()
    reviewCount = 0
    linkCount = 0
    bookCount = 0
    fullList = []
    for i in range(1):
        bsObj = goodreads.crawl(url + "list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page=" + str(i))
        linkList = goodreads.getLinks(bsObj, fullList)
    books = {};
    for i in range(len(linkList)):
        bsObj = goodreads.crawl(url + str(linkList[i]))
        goodreads.getBook(bsObj)
