#!/usr/bin/python3
"""
This script initializes a FileStorage instance and reloads data,
making it available for managing and persisting data.
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
