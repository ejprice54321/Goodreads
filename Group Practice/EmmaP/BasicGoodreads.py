##################
# This crawler gets the url of a popular book list from Goodreads,
# and prints out the titles and authors from the first 5 pages
#################

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

class Book:
    'Common base class for all articles/pages'
    def __init__(self, title, author, url):
        self.title = title;
        self.author = author;
        self.url = url;
      

class Crawler:

    def crawlURL(self, site, url):
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
                table = bsObj.find("table", {"class":"tableList"})
                book = table.findAll("tr")
                for tr in book:
                    cols = tr.findAll('td')
                    link = cols[1].find("a").get('href')
                    print(link)
                # for book in bookList:
                #     print(genre.get_text())

    def crawlTitle(self, site, url):
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
                titleList = bsObj.findAll("span", {"itemprop" : "name"})
                for title in titleList[::2]
                    print(title.get_text())

    def crawlAuthor(self, site, url):
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
                authorList = bsObj.findAll("span", {"itemprop" : "name"})
                for author in authorList[1::2]
                    print(author.get_text())


if name == "__main__":
    
crawlBookList("https://www.goodreads.com/list/show/1381.Best_Series?page=")