#!/usr/bin/env python3
"""Update all topics"""


def update_topics(mongo_collection, name, topics):
    """Update all topics of a document"""
    doc = mongo_collection.update_one({"name": name},
                                      {"$set": {"topics": topics}})

    return doc
