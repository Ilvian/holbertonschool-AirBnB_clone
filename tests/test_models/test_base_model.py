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
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    '''
    This script initializes a FileStorage instance and reloads data,
    making it available for managing and persisting data.
    '''

    def test_attributes(self):
        '''
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        '''

        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)
        self.assertNotEqual(base1.created_at, base2.created_at)
        self.assertNotEqual(base1.updated_at, base2.updated_at)

    def test_attribute_type(self):
        '''
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        '''

        base1 = BaseModel()
        self.assertEqual(type(base1.id), str)
        self.assertEqual(type(base1.created_at), datetime.datetime)
        self.assertEqual(type(base1.updated_at), datetime.datetime)

    def test_storage(self):
        '''
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        '''

        base = BaseModel()
        self.assertNotEqual(len(storage.all()), 0)

    def test_save(self):
        '''
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        '''

        base = BaseModel()
        time = base.save()
        self.assertEqual(base.updated_at, time)

    def test_to_dict(self):
        '''
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        '''

        base = BaseModel()
        new_d = base.to_dict()
        self.assertEqual(new_d['id'], base.id)
        self.assertEqual(new_d['created_at'], base.created_at.isoformat())
        self.assertEqual(new_d['updated_at'], base.updated_at.isoformat())

    def test_to_str(self):
        '''
        This script initializes a FileStorage instance and reloads data,
        making it available for managing and persisting data.
        '''

        base = BaseModel()
        expected_output = f"[{base.__class__.__name__}] ({base.id}) {base.__dict__}"
        self.assertEqual(str(base), expected_output)

