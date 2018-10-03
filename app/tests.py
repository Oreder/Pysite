from django.test import TestCase
from django.test import Client

# Create your tests here.

class ViewTest(TestCase):
	def testAppView(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)
	
	def testProfile(self):
		resp = self.client.post('/', {'user': 'Oreder'} )
		self.assertEqual(resp.status_code, 200)

	def testProfileContent(self):
		resp = self.client.post('/', {'user': 'sherk'} )
		self.assertNotEqual(resp.content, '')