##################
# This class holds a title, author and url link from Goodreads.
#################

import pymysql
from pymysql.err import InternalError

class Book:
    def __init__(self, id, title, author, bookUrl):
        self.title = title
        self.author = author
        self.bookUrl = bookUrl
        # self.description = description
        # self.rating = rating
        # self.characters = characters
        # self.setting = setting
        # self.awards = awards

    def save(self, db):

    		try:
    			db.cur.execute("SELECT * FROM books WHERE titleId = %s AND authorId = %s", (int(self.title.id), int(self.author.id)))

    			if db.cur.rowcount == 0:
    				print("INSERT INTO books (titleId, authorId) VALUES ("+str(self.question.id)+", "+str(self.player.id)+")")
    				db.cur.execute("INSERT INTO books (titleId, authorId) VALUES (%s, %s)", (int(self.question.id), int(self.player.id)))
    				db.conn.commit()
    				self.id = db.cur.lastrowid
    			else:
    				self.id = db.cur.fetchall()[0]["id"]

    		except InternalError as e:
    			print("INSERT INTO books (titleId, authorId) VALUES ("+str(self.question.id)+", "+str(self.player.id)+")")

    			print("Internal error!")
    			print(e)
    			db.conn.rollback()


    		return self
