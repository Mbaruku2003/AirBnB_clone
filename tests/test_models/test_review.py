#!/usr/bin/python3
"""Define a test class."""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Define a testcase."""

    def test_review_attributes(self):
        """Define test for attributes."""

        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
