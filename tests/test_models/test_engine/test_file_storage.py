#!/usr/bin/python3
"""Test for file storage"""


import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Create an instance of FileStorage
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up and delete the test JSON file if it exists
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_storage(self):
        self.assertEqual(type(self.storage.all()), dict)

    def test_filepath(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        self.assertEqual(type(self.storage._FileStorage__objects), dict)
        self.assertEqual(self.storage._FileStorage__objects, self.storage.all())

    def test_new(self):
        user = User()
        self.storage.new(user)
        self.assertTrue("User.{}".format(user.id) in self.storage.all())

    def test_save_reload(self):
        user = User()
        self.storage.new(user)
        self.storage.save()

        # Create a new storage instance and load the data
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the object is successfully loaded
        self.assertTrue("User.{}".format(user.id) in new_storage.all())

    def test_all(self):
        user = User()
        self.storage.new(user)
        self.assertEqual(self.storage.all(), {"User.{}".format(user.id): user})


if __name__ == '__main__':
    unittest.main()
