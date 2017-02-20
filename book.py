##################
# This class holds a title, author, description, bookType, pages, rating, characters,
# awards, and publication for each book object from Goodreads.
#################
from database import Database
import pymysql
from pymysql.err import InternalError

class Book:

    def __init__(self, url, title, author, description, pages, rating, characters, awards, publication):
        self.url = url
        self.title = title
        self.author = author
        self.description = description
        self.pages = pages
        self.rating = rating
        self.characters = characters
        self.awards = awards
        self.publication = publication

    def save(self, db):

            add_book = ("INSERT INTO book "
                        "(url, title, author, description, pages, rating, characters, awards, publication) "
                        "VALUES (%s, %s, %s, %s, %i, %i, %s, %s, %s)")

            data_book = (self.url, self.title, self.author, self.description, self.pages, self.rating, self.characters, self.awards, self.publication)

            #Insert book
            db.cur.execute(add_book, data_book)
            #commit data to Database
            db.conn.commit()