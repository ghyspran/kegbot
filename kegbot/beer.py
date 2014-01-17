import sqlite3

import time

def find_beer(search_type, value):
  if (search_type == 'id'):
    return load_remote_beer(value)
  elif (search_type == 'name'):
    return search_remote_beer(value)
  else:
    return None

class Beer:
  """A beer that can be placed into a keg."""

  def __init__(self, properties):
    for (key, value) in properties:
      if hasattr(self, key):
        self.key = value
    self.synced = time.time()

  def
