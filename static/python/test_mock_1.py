import unittest
from unittest.mock import MagicMock
import requests

def get_condition(city):
    response = requests.get(f'https://weather.com/{city}')
    weather = response.json()
    return weather["condition"]

class TestWeatherApp(unittest.TestCase):
    def setUp(self):
        self.get_patcher = unittest.mock.patch('requests.get')
        self.mock_get = self.get_patcher.start()

    def tearDown(self):
        self.get_patcher.stop()

    def test_get_weather(self):
        self.mock_get.return_value.json.return_value = {'temperature': 72, 'condition': 'sunny'}
        weather = get_condition('San Francisco')
        self.assertEqual(weather, 'sunny')
