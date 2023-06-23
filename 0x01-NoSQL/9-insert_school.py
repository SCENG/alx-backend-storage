#!/usr/bin/env python3


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection
    based on keyword arguments.

    Args:
        mongo_collection: The MongoDB collection object.
        **kwargs: Keyword arguments representing the fields
        and values of the document.

    Returns:
        str: The _id of the newly created document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
