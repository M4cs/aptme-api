import unittest
import requests
import json
from app import app

class APITests(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        
    def test_1_heartbeat(self):
        rv = self.app.get('/api')
        self.assertEqual(rv.status_code, 200)
    
    def test_2_top(self):
        rv = self.app.get('/api/top')
        self.assertEqual(rv.status_code, 200)
        
    def test_3_search_cached_not_on(self):
        rv = self.app.get('/api/repo?search=https://apt.securarepo.io')
        self.assertEqual(rv.status_code, 200)
    
    def test_4_search_cached_on(self):
        rv = self.app.get('/api/repo?search=https://apt.securarepo.io&force_cache=on')
        self.assertEqual(rv.status_code, 200)
        
    def test_5_packages_2_json(self):
        rv = self.app.get('/api/package2json?repo=https://apt.securarepo.io')
        response_json = json.loads(rv.data)
        for i in range(len(response_json)):
            self.assertTrue('name' in response_json[i])
            self.assertTrue('author' in response_json[i])
            self.assertTrue('download_link' in response_json[i])
            self.assertTrue('version' in response_json[i])
            self.assertTrue('description' in response_json[i])
            self.assertTrue('maintainer' in response_json[i])
            self.assertTrue('depiction' in response_json[i])
        self.assertEqual(rv.status_code, 200)

if __name__ == '__main__':
    unittest.main()