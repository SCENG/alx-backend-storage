#!/usr/bin/env python3


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Returns:
        list: A list containing all the documents in the collection.
    """
    return mongo_collection.find()
