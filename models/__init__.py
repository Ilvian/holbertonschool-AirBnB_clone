#!/usr/bin/python3
"""
This script initializes a FileStorage instance and reloads data from a JSON file.
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
