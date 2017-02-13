##################
# This class holds a book, reviewer, review, number of likes,
# date reviewed, and rating content from Goodreads.
#################

import pymysql
from pymysql.err import InternalError

class Review:
    def __init__(self, book, reviewer, content, likes, date, rating = 0):
    	self.book = book
    	self.reviewer = reviewer
    	self.content = content
    	self.likes = likes
    	self.date = date
    	self.rating = rating