##################
# This class holds a title, author and url link from Goodreads.
#################
from database import Database
import pymysql
from pymysql.err import InternalError

class Book:

    def __init__(self, title, author, description, bookType, pages = 0, rating = 0, characters = 0, awards = 0, publication = 0):
        self.title = title
        self.author = author
        self.description = description
        self.bookType = bookType
        self.pages = pages
        self.rating = rating
        self.characters = characters
        self.awards = awards
        self.publication = publication

    def save(self, db):

            add_book = ("INSERT INTO books "
                        "(title, author) "
                        "VALUES (%s, %s)")

            data_book = (self.title, self.author)

            #Check to see if book already EXISTS
            

            #Insert book
            db.cur.execute(add_book, data_book)

            #commit data to Database
            db.conn.commit()
