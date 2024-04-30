#!/usr/bin/env python3
"""task 8
"""

def list_all(mongo_collection):
    """Function that lists all documents in a collect


    Args:
        mongo_collection (pymongo.collection.Collection): collection to analyze

    Returns:
        list:  all documents in a collection 
    """
    return [doc for doc in mongo_collection.find()]
