##################
# This crawler gets the Best Series book list from Goodreads,
# and prints out the titles and authors from the first 5 pages
#################

from urllib.request import urlopen
from bs4 import BeautifulSoup

for i in range(0, 5):
    print("Scraping page: "+str(i)+" of Best Series book list")
    url = "https://www.goodreads.com/list/show/1381.Best_Series?page="+str(i)
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")
    genreList = bsObj.findAll("span", {"itemprop":"name"})
    for genre in genreList:
        print(genre.get_text())