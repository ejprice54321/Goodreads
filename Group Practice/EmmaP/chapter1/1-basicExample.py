from urllib.request import urlopen
#Retrieve HTML string from the URL
html = urlopen("https://www.goodreads.com/search?utf8=%E2%9C%93&query=book")
print(html.read())