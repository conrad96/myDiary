import unittest
import app
import json

class TestApi(unittest.TestCase):

	def setUp(self):
		self.app=app.app.test_client()
		self.entry_id=1
		'''test all entries response'''
	def test_allEntries(self):
		response=self.app.get('/api/v1/entries/')
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.content_type,'application/json')

	def test_addEntry(self):
		response=self.app.post('/api/v1/entries/')
		self.assertTrue(response.status_code,200)
		 	

if __name__=='__main__':
	unittest.main()		