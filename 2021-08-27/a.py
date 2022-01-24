import unittest

from view import get_city_info



class CitiesTestCase(unittest.TestCase):
    """测试city_functions.py"""
    def test_city_country(self):
        city_info = get_city_info('shanghai', 'china')
        self.assertEqual(city_info, 'Shanghai, China')

    def test_New_York(self):
        city_info = get_city_info('new york', 'America')
        self.assertEqual(city_info, 'New York, America')


if __name__ == '__main__':
    unittest.main()