from multiprocessing.connection import Client
from urllib import response
from django.test import TestCase

class UnitTestingMyWatchlist(TestCase):
    def unit_testing_html(self):
        response = Client.get('')
        self.assertEqual(response.status_code,200)
        
# Create your tests here.