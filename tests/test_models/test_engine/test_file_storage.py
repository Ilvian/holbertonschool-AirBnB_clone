#!/usr/bin/python3
"""test for file storage"""


import unittest
import os
from models.base_model import BaseModel
from models.user import User
from file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Create an instance of FileStorage
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up and delete the test JSON file if it exists
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_new(self):
        # Test adding a new object to the storage
        user = User()
        self.storage.new(user)
        self.assertTrue("User.{}".format(user.id) in self.storage.all())

    def test_save_reload(self):
        # Test saving and reloading objects
        user = User()
        self.storage.new(user)
        self.storage.save()

        # Create a new storage instance and load the data
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the object is successfully loaded
        self.assertTrue("User.{}".format(user.id) in new_storage.all())

    def test_all(self):
        # Test the all() method
        user = User()
        self.storage.new(user)
        self.assertEqual(self.storage.all(), {"User.{}".format(user.id): user})


if __name__ == '__main__':
    unittest.main()
