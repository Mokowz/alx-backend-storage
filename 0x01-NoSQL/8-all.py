#!/usr/bin/env python3
# List all documents

import pymongo


def list_all(mongo_collection):
  """ lists all documents in a collection """
  cursor = db.mongo_collection.find()

  return cursor
