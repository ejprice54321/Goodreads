##################
# This crawler gets the url of a popular book list from Goodreads,
# and prints out the titles and authors from the first 5 pages
#################

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

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
            for genre in genreList:
                print(genre.get_text())

crawlBookList("https://www.goodreads.com/list/show/1381.Best_Series?page=")