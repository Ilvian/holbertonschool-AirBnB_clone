#!/usr/bin/python3
"""
Unittests for FileStorage class
"""


import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        self.user = User()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_storage(self):
        self.assertIsInstance(self.storage, FileStorage)

    def test_new(self):
        self.storage.new(self.model)
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, self.storage.all().keys())

    def test_save(self):
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, self.storage.all().keys())

    def test_save_user(self):
        self.storage.new(self.user)
        key = "{}.{}".format(self.user.__class__.__name__, self.user.id)
        self.assertIn(key, self.storage.all().keys())


if __name__ == '__main__':
    unittest.main()
