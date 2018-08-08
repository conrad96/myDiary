import unittest
import app
import json

class TestApi(unittest.TestCase):

	def setUp(self):
		self.app=app.app.test_client()
		self.entry_id=1
		self.user_id=8

		'''test all entries response'''
	def test_allEntries(self):
		response=self.app.get('/api/v1/entries/')
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.content_type,'application/json')

		'''test new entry'''
	def test_addEntry(self):
		response=self.app.post('/api/v1/entries/[]'.format(self.entry_id))
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.content_type,'application/json')

		'''test search single entry'''	
		
	def test_searchEntry(self):
		data={
		"entry_id":'1',
		"username":'Bill12',
		"title":'My Day 1',
		"body":'Dear Diary Today was so exhausting 1',
		"date":'7-23-2018'
		}
		response=self.app.get('/api/v1/entries/[]'.format(self.entry_id),data=json.dumps(data),content_type='application/json',follow_redirects=True)
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.content_type,'application/json')
		json_response=json.loads(response.get_data(as_text=True))
		self.assertTrue(json_response,data)

		'''test modifying an  entry'''		
	def test_modifyEntry(self):
		data={
		"entry_id":'1',
		"username":'bill123',
		"title":'My Day 1 edit',
		"body":'Dear Diary Today was so exhausting 1 edited',
		"date":'7-23-2018'
		}
		response=self.app.put('/api/v1/entries/[]'.format(self.entry_id),data=json.dumps(data),content_type='application/json',follow_redirects=True)
		self.assertEqual(response.status_code,200)
		json_response=json.loads(response.get_data(as_text=True))
		self.assertTrue(json_response,data)	
		
		'''test adding new user'''
	def test_addUser(self):
		response=self.app.post('/api/v1/users/[]'.format(self.user_id))
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.content_type,'application/json')
	
			
if __name__=='__main__':
	unittest.main()		