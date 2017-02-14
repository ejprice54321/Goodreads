##################
# This class holds a rating, reviewer, and review content from Goodreads.
#################

import pymysql
from pymysql.err import InternalError

class Author:
    def __init__(self, name, website, birth, death,bio):
    	self.name = name
    	self.website = website
    	self.birth = birth
    	self.death = death
    	self.bio = bio


    # def save(self, db):
    #
    #     add_author = ("INSERT INTO books "
    #                 "(name, website, birth, death, bio) "
    #                 "VALUES (%s, %s, %s, %s, %s)")
    #
    #     data_author = (self.name, self.website, self.birth, self.death, self.bio)
    #
    #     #Check to see if book already exists
    #     db.cur.execute("SELECT * FROM authors WHERE name = %s", (str(self.name)))
    #     if db.cur.rowcount == 0:
    #     	#Insert author
    #     	db.cur.execute(add_author, data_author)
    #
    #     	#commit data to Database
    #     	db.conn.commit()
    def save(self, db):
        #


        add_author = ("INSERT INTO authors "
                        "(name, website, birth, death, bio) "
                        "VALUES (%s, %s, %s, %s, %s)")
        #
        data_author = (self.name, self.website, self.birth, self.death, self.bio)

        #Check to see if author already exists

        #Insert author
        db.cur.execute(add_author, data_author)

        #commit data to Database
        db.conn.commit()

        # try:
        #     db.cur.execute("SELECT * FROM authors WHERE authorID = %s", (str(self.name)))
        #     if db.cur.rowcount == 0:
        #         db.cur.execute(add_author, data_author)
        #         db.conn.commit()
        #         self.name = db.cur.lastrowname
        #     else:
        #         self.name = db.cur.fetchall()[0]["name"]
        # except InternalError as e:
        #     print("no")
        #     db.conn.rollback()
        # return self
