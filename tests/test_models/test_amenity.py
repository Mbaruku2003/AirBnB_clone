#!/user/bin/python3
"""Define a class amenity."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity_attributes(self):
        """Tests for amenity."""

        amenity = Amenity()
        self.assertEqual(amenity_name, "")