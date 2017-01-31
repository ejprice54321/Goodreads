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

def getTitle(bsObj):
    genreList = bsObj.findAll("span", {"itemprop":"name"})
    for title in genreList[::2]:
        return title.get_text()


def getAuthor(bsObj):
    genreList = bsObj.findAll("span", {"itemprop":"name"})
    for author in genreList[1::2]:
        return author.get_text()

def getHref(bsobj):
    table = bsObj.find("table", {"class":"tableList"})
    book = table.findAll("tr")
    for tr in book:
        cols = tr.findAll("td")
        link = cols[1].find("a").get("href")
        return link


if __name__ == "__main__":
    url = "https://www.goodreads.com/list/show/1381.Best_Series?page="
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
            print(getTitle(bsObj))