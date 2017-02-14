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


    def save(self, db):

            add_review = ("INSERT INTO books "
                        "(book, reviewer, content, likes, date, rating) "
                        "VALUES (%s, %s, %s, %s, %s, %s)")

            data_review = (self.book, self.reviewer, self.content, self.likes, self.date, self.reviewer)

            #Check to see if book already exists

            #Insert author
            db.cur.execute(add_review, data_review)

            #commit data to Database
            db.conn.commit()