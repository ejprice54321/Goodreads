##################
# This crawler gets the url of a popular book list from Goodreads,
# and prints out the titles and authors from the first 5 pages
#################

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

class Book:
    def __init__(self, title, author, url):
        self.title = title
        self.author = author
        self.url = url

def crawlBookList(url):
    for i in range(0, 5):
        try:
            html = urlopen(url+str(i))
        except HTTPError as e:
            print(e)
        except URLError as e:
            print("The server could not be found!")
        else:
            print("Scraping page: "+str(i)+" of Best Series book list")
            bsObj = BeautifulSoup(html, "html.parser")
            genreList = bsObj.findAll("span", {"itemprop":"name"})
            for title in genreList[::2]:
                book = Book()
                print(genre.get_text())

            for author in genreList[1::2]:
                print(author.get_text())




crawlBookList("https://www.goodreads.com/list/show/1381.Best_Series?page=")