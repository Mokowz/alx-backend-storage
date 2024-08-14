#!/usr/bin/env python3
# Insert a document in Python


def insert_school(mongo_collection, **kwargs):
    """ inserts a new doc"""
    cursor = mongo_collection.insert_one(**kwargs)
    return cursor.inserted_id
