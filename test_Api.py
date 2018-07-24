import unittest
import app
import json

class TestApi(unittest.TestCase):

	def setUp(self):
		self.app=app.app.test_client()
		self.entry_id=1

	def test_allEntries(self):
		response=self.app.get('/api/v1/entries/')
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.content_type,'application/json')

	def test_addEntry(self):
		response=self.app.post('/api/v1/entries/')
		self.assertEqual(response.status_code,200)

	# def test_allEntries(self):
	# 	response=self.app.get('/api/v1/entries/')
	# 	self.assertEqual(response.status_code,200)
	# 	self.assertEqual(response.content_type,'application/json')		

if __name__=='__main__':
	unittest.main()		