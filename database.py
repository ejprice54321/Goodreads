import pymysql
from pymysql.err import InternalError

class Database:

	def __init__(self):
		self.conn = pymysql.connect(user='ewesterhoff', passwd='', charset='utf8')
		self.cur = self.conn.cursor()
		self.cur.execute("USE goodreads")
