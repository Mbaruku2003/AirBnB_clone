#!/user/bin/python3
"""Define test class."""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Define a test class."""

    def test_user_attributes(self):
        """Define a test for users."""

        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
