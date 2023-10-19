#!/usr/bin/env python3
""" lists all documents in a collection """


def list_all(mongo_collection):
    """
    Function that lists all documents in a collection

    Args
		mongo_collection - a pymongo collection
    """
    return mongo_collection.find()
