#!/usr/bin/python3
"""
This script defines a BaseModel class for managing and persisting data.
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

