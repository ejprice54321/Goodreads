from urllib.request import urlopen

html = urlopen("http://www.olin.edu")
print(html.read())
