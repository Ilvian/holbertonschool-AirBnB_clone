#!/usr/bin/python3
'''
This script initializes a FileStorage instance and reloads data,
making it available for managing and persisting data.
'''


import io
import sys
import unittest
import os
import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    '''
    This script initializes a FileStorage instance and reloads data,
    making it available for managing and persisting data.
    '''

    def test_storage(self):
        '''
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        '''

        obj = FileStorage()
        self.assertEqual(type(obj.all()), dict)

    def test_filepath(self):
        '''
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        '''

        obj = FileStorage()
        self.assertEqual(obj._FileStorage__file_path, "file.json")

    def test_objects(self):
        '''
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        '''

        obj = FileStorage()
        self.assertEqual(type(obj._FileStorage__objects), dict)
        self.assertEqual(obj._FileStorage__objects, obj.all())

    def test_methods(self):
        '''
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        '''

        obj = FileStorage()
        base = BaseModel()
        result = obj.new(base)
        self.assertTrue(result is not None)
        result = obj.save()
        self.assertTrue(result is not None)
        result = obj.reload()
        self.assertTrue(result is not None)
