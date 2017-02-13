import pymysql
from pymysql.err import InternalError

class Database:

	def __init__(self):
		#Assumes port 3306
		#self.conn = pymysql.connect(user='root', passwd='root', charset='utf8')
		self.conn = pymysql.connect(user='ewesterhoff', passwd='', charset='utf8')
		self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
		self.cur.execute("USE goodreads")
