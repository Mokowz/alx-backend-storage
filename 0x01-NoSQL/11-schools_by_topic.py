#!/usr/bin/env python3
"""School by topic"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    cursor = mongo_collection.find({"topics": topic})
    return cursor
