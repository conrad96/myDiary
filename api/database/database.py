import psycopg2
from pprint import pprint
import os,sys

class DB_Connection():
	def __init__(self):
		self.connection=psycopg2.connect("dbname='myDiary' user='postgres' password='715' port='5432' ")
		self.cursor=self.connection.cursor()

	def addUser(self,fullnames,username,password):
		self.cursor.execute("INSERT INTO users(user_id,fullnames,username,password) VALUES( DEFAULT,%s,%s,%s)",(fullnames,username,password))
		self.connection.commit()
		self.cursor.close()
		
db=DB_Connection()
db.addUser("mark cuban","cuban12","qwerty")	