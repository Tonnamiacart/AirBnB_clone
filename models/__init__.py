#!/usr/bin/python3
"""
The __init__ file primary purpose is to initialise file
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
