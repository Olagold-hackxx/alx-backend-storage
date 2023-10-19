#!/usr/bin/env python3
""" Inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Function that inserts a new document in a collection based on kwargs

    Args
		mongo_collection - a pymongo collection
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
