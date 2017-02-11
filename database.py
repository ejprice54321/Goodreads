import pymysql
from pymysql.err import InternalError

class Database:

	def __init__(self):
		#Assumes port 3306
		self.conn = pymysql.connect(host='127.0.0.1', unix_socket='/run/mysqld/mysqdl.sock', user='root', passwd='root', db='mysql', charset='utf8')
		self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
		self.cur.execute("USE goodreadsCrawler")