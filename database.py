import psycopg2
import psycopg2.extras as ex
import os,sys,json
import jsonify
import datetime
class Database:
	def __init__(self):
		self.connection=psycopg2.connect("dbname='myDiary' user='postgres' password='715' port='5432' ")
		self.cursor=self.connection.cursor()

	'''Method to add/register user account '''
	def addUser(self,fullnames,username,password):
		try:
			self.cursor.execute("INSERT INTO users(user_id,fullnames,username,password) VALUES( DEFAULT,%s,%s,%s)",(fullnames,username,password))
			self.connection.commit()
			return True
		except psycopg2.Error as e:
			print(e.pgerror)
			return False
	'''Method to Login user by validating the username and password '''			
	def loginUser(self,username,password):
		try:
			self.cursor=self.connection.cursor(cursor_factory=ex.DictCursor)
			self.cursor.execute("SELECT * FROM users WHERE username='"+username+"' AND password='"+password+"' ")
			rows=self.cursor.fetchall()
			if  rows!=[] :				
				return True
			else:
			 	return False
		except psycopg2.Error as e:
			print(e.pgerror)

	'''Method to retrieve all users '''			
	def getUsers(self):
		try:
			self.cursor=self.connection.cursor(cursor_factory=ex.DictCursor)
			self.cursor.execute("SELECT * FROM users ")
			rows=self.cursor.fetchall()
			if  rows!=[] :				
				return rows
			else:
			 	return False
		except psycopg2.Error as e:
			print(e.pgerror)

	'''Method to add a single Entry into the DB'''		
	def addEntry(self,user_id,title,body,date_posted):			
		try:
			self.cursor=self.connection.cursor(cursor_factory=ex.DictCursor)
			self.cursor.execute("INSERT INTO entries (user_id,title,body,date_posted,entry_id) VALUES( %s,%s,%s,%s,DEFAULT)",(user_id,title,body,date_posted))
			self.connection.commit()
			return True
		except psycopg2.Error as e:
			print(e.pgerror)
			return False

	'''Method to fetch all Entries in the Database'''		
	def getEntries(self):
		try:
			self.cursor=self.connection.cursor(cursor_factory=ex.DictCursor)
			self.cursor.execute("SELECT * FROM entries")
			rows=self.cursor.fetchall()
			if  rows!=[] :				
				return rows
			else:
			 	return False
		except psycopg2.Error as e:
			return e.pgerror	

	'''Method to fetch all a users Entries basing on his user_id'''		
	def getuserEntries(self,user_id):
		try:
			self.cursor=self.connection.cursor(cursor_factory=ex.DictCursor)
			self.cursor.execute("SELECT * FROM entries WHERE user_id='"+user_id+"' ")
			rows=self.cursor.fetchall()
			if  rows!=[] :				
				return rows
			else:
			 	return False
		except psycopg2.Error as e:
			return e.pgerror				

	def modifyEntry(self,entry_id,title,body,date):
		try:
			self.cursor=self.connection.cursor(cursor_factory=ex.DictCursor)
			self.cursor.execute("UPDATE entries SET  title=%s , body=%s , date_posted=%s  WHERE entry_id='"+entry_id+"' ",(title,body,date))
			updated_rows = self.cursor.rowcount
			self.connection.commit()
			return True
		except psycopg2.Error as e:
			print(e.pgerror)
			return False
				
	def getDate(self,entry_id):
		try:
			entry_id=str(entry_id)
			self.cursor=self.connection.cursor(cursor_factory=ex.DictCursor)
			self.cursor.execute("SELECT row_to_json(t) FROM ( select date_posted from entries where entry_id='"+entry_id+"' ) t ")
			rows=self.cursor.fetchall()
			if  rows!=[] :
				datePost=""
				for y in rows:
					for z in y:
						datePost=z['date_posted']
				return datePost
			else:
			 	return False
			self.connection.commit()
			return True
		except psycopg2.Error as e:
			print(e.pgerror)
			return False		
db=Database()
# x=db.getDate(3)
# print(type(x))

#x=db.modifyEntry("3","Love","I love this girl","2018-07-02")
#print(x)			
now = datetime.datetime.now()
# yr="%d" %now.year
# mnth="%d"%now.month
# day="%d"%now.day
date= now.strftime("%Y-%m-%d")
print(date)