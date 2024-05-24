import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_add(self):
        response = self.client.post('/api/add', json={'a': 5, 'b': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 8)

if __name__ == '__main__':
    unittest.main()
