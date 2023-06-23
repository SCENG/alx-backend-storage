#!/usr/bin/env python3


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: The MongoDB collection object.
        topic (str): The topic to search.

    Returns:
        List[dict]: The list of schools matching the
        specified topic.

    """
    return mongo_collection.find({"topics": topic})
