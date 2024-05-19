#!/usr/bin/python3
"""Define a test class."""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Define a test class."""

    def test_city_attributes(self):
        """Define test_city."""

        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == "__main__":
    unittest.main()
