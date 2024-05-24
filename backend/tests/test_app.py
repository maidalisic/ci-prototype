import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
import unittest

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, World!', response.data.decode())

    def test_calculate(self):
        # Test for correct calculation
        response = self.client.post('/api/calculate', json={'expression': '1+3*3*(3+4*2)'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 100)  # Expected result of the expression

        # Test for complex calculation
        response = self.client.post('/api/calculate', json={'expression': '2*(2+3)*2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 20)  # Expected result of the expression

        # Test for incorrect expression
        response = self.client.post('/api/calculate', json={'expression': '2*/3'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()
