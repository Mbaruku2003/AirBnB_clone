#!/usr/bin/python3
"""Define adding of a function."""
import unittest
from add import add


class TestAddFunction(unittest.TestCase):
    """Test czase for add function."""

    def test_add_pos_numbers(self):
        """Test case for positive numbers."""

        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        """Test for negativ numbers."""

        self.assertEqual(add(-1, -2), -3)

    def test_add_zero(self):
        """Test add with zero."""

        self.assertEqual(add(0, 0), 0)

    def test_add_default_values(self):
        """Test add with default values."""

        self.assertEqual(add(), 1)

    def add_mixed_signs(elf):
        """Test add with mixed signs."""

        self.assertEqual(add(-1, 1), 0)

    def test_add_floats(self):
        """Test add with floats."""
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)
