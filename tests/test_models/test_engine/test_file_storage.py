#!/usr/bin/python3
"""Define class."""
import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """instances to be used by all methods."""

        self.storage = FileStorage()
        self.file_path = "file.json"
        self.storage._FileStorage__file_path = self.file_path
        self.obj = BaseModel()
        self.obj_key = f"BaseModel.{self.obj.id}"

    def tearDown(self):
        """Destroys instances."""

        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Tests all."""

        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Tests for new instances."""

        self.storage.new(self.obj)
        self.assertIn(self.obj_key, self.storage.all())

    def test_save(self):
        """Test for new objects."""

        self.storage.new(self.obj)
        self.storage.save()
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            self.assertIn(self.obj_key, data)

    def test_reload(self):
        """Tests for reload."""

        self.storage.new(self.obj)
        self.storage.save()
        self.storage.reload()
        self.assertIn(self.obj_key, self.storage.all())
