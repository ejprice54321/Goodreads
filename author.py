##################
# This class holds a name, website, date of birth, date of death, and biography for each author object from Goodreads.
#################

import pymysql
from pymysql.err import InternalError

class Author:
    def __init__(self, url, name, website, birth, death,bio):
        self.url = url
        self.name = name
        self.website = website
        self.birth = birth
        self.death = death
        self.bio = bio

    def save(self, db):

        add_author = ("INSERT INTO author "
                        "(url, name, website, birth, death, bio) "
                        "VALUES (%s, %s, %s, %s, %s, %s)")
    
        data_author = (self.url, self.name, self.website, self.birth, self.death, self.bio)

        #Insert author
        db.cur.execute(add_author, data_author)
        #commit data to Database
        db.conn.commit()
