#!/usr/bin/python3
"""Tests for state."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Define the class."""

    def test_state_attributes(self):
        """Define the taste state."""

        state = State()
        self.assertEqual(state.name, "")
