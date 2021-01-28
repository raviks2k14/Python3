import unittest
from city_functions import city_country


class CitiesToTest(unittest.TestCase):
    """"Tests for 'city_functions.py'"""

    def test_city_country_without_population(self):
        """Send city, country details from here"""
        returned_value = city_country('santiago', 'chile')
        self.assertEqual(returned_value, "Santiago, Chile")

    def test_city_country_population(self):
        """Send city, country details from here"""
        returned_value = city_country('santiago', 'chile', 5000000)
        self.assertEqual(returned_value, "Santiago, Chile - population 5000000")


if __name__ == '__main__':
    unittest.main()
