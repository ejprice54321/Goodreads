##################
# This class holds a rating, reviewer, and review content from Goodreads.
#################

import pymysql
from pymysql.err import InternalError

class Author:
    def __init__(self, name, website, bio, birth, death = 0):
    	self.name = name
    	self.website = website
    	self.birth = birth
    	self.death = death
    	self.bio = bio


    def save(self, db):

            add_author = ("INSERT INTO books "
                        "(name, website, birth, death, bio) "
                        "VALUES (%s, %s, %s, %s, %s)")

            data_author = (self.name, self.website, self.birth, self.death, self.bio)

            #Check to see if book already exists

            #Insert author
            db.cur.execute(add_author, data_author)

            #commit data to Database
            db.conn.commit()