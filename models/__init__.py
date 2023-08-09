#!/usr/bin/python3
"""Initialize models directory with FileStorage instance and reload data."""

from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()

# Reload the storage data
storage.reload()
