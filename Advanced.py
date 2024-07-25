import unittest
from unittest.mock  import patch

def grt_data():
    import requests
    response = requests.get('https://api.example.com/data')
    return response.json()

class testGetData(unittest.TestCase):
    @patch('requests.get')
    def test_get_data(self, mock_get):
        mock_get.return_value.json.return_value = {'key': 'value'}
        result = grt_data()
        self.assertEqual(result, {'key': 'value'})

if __name__ == '__main__':
    unittest.main()        