from multiprocessing.connection import Client
from django.test import TestCase
import requests

class UnitTestingMyWatchlist(TestCase):
    def test_html(self):
        response = requests.get('http://pbpshafa.herokuapp.com/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_xml(self):
        response = requests.get('http://pbpshafa.herokuapp.com/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
    
    def test_json(self):
        response = requests.get('http://pbpshafa.herokuapp.com/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

# Create your tests here.