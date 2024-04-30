#!/usr/bin/env python3
"""task 10
"""

def update_topics(mongo_collection, name, topics):
    """Function that changes all topics of a school document based on name.

    Args:
        mongo_collection (pymongo.collection.Collection): collection to analyze
        name : school name to update
        topics : ist of topics approached in the school.
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
