import unittest
import json
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data, b'Hello, World!', )
        
    def test_get_all(self):
        response = self.app.get('/task')
        self.assertEqual(response.status_code, 200)
        
    def test_creat(self):
        data = {
            'name': '買晚餐',
        }
        response = self.app.post("/task", 
                                data=json.dumps(data), 
                                content_type='application/json',
                            )
        self.assertEqual(response.status_code, 201)

    def test_update(self):
        data = {
            'name': '買晚餐_test',
            'status': 0
        }
        response = self.app.put("/task/2", 
                                data=json.dumps(data), 
                                content_type='application/json',
                            )
        self.assertEqual(response.status_code, 200)
        
    def test_update_not_exist(self):
        data = {
            'name': '買晚餐_test',
            'status': '0'
        }
        response = self.app.put("/task/12342", 
                                data=json.dumps(data), 
                                content_type='application/json',
                            )
        self.assertEqual(response.status_code, 200)
         
    def test_delete(self):
        response = self.app.delete('/task/1')
        self.assertEqual(response.status_code, 200)
        
    def test_delete_not_exist(self):
        response = self.app.delete('/task/123')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
