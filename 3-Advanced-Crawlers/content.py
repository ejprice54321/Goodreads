class Content:
   'Common base class for all articles/pages'


   def __init__(self, title, author, url):
      self.title = title;
      self.author = author;
      self.url = url;
      