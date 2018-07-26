import psycopg2
import psycopg2.extras as ex
import os,sys,json
import jsonify

class Database():
	def __init__(self):
		self.connection=psycopg2.connect("dbname='myDiary' user='postgres' password='715' port='5432' ")
		self.cursor=self.connection.cursor()

	'''function to add/register user account '''
	def addUser(self,fullnames,username,password):
		try:
			self.cursor.execute("INSERT INTO users(user_id,fullnames,username,password) VALUES( DEFAULT,%s,%s,%s)",(fullnames,username,password))
			self.connection.commit()
			self.cursor.close()
		except psycopg2.Error as e:
			print(e.pgerror)
	'''function to Login user '''			
	def loginUser(self,username,password):
		try:
			self.cursor=self.connection.cursor(cursor_factory=ex.DictCursor)
			self.cursor.execute("SELECT * FROM users WHERE username='"+username+"' AND password='"+password+"' ")
			rows=self.cursor.fetchall()
			if  rows!=[] :				
				return rows
			else:
			 	return False
		except psycopg2.Error as e:
			print(e.pgerror)			

db=Database()
#db.addUser("mark cuban","cuban12","qwerty")
output=db.loginUser('conrad96','qwerty')	
print(output)
