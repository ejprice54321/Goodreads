class Content:
   'Common base class for all articles/pages'


   def __init__(self, id, topicId, title, url):
      self.id = id
      self.topicId = topicId;
      self.title = title;
      self.url = url;
      