#!/usr/bin/python3
"""Define testsing class."""
import uuid
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """Define a class."""

    def test_attributes(self):
        """Define testing attributes."""

        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertEqual(type(obj.id), str)
        self.assertEqual(type(obj.created_at), datetime)
        self.assertEqual(type(obj.updated_at), datetime)
        
    def test_unique_id(self):
        """Test id."""

        obj1.BaseModel()
        obj2.BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_str_method(self):
        """Test str method."""

        obj = BaseModel()
        self.assertEqual(str(obj), f"[BaseModel] ({obj.id}) {obj.__dict__}")

    def test_save_method(self):
        """Define method to save."""

        obj = BaseModel()
        updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(updated_at, obj.updated_at)

    def test_to_dict(self):
        """Test for dict representation."""

        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(type(obj_dict['created_at']), str)
        self.assertEqual(type(obj_dict['updated_at']), str)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['created_at'], obj.updated_at.isoformat())
