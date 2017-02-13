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