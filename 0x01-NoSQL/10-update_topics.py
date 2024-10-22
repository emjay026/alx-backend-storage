#!/usr/bin/env python3
"""
This module provides a function to update the topics of a school document
in a MongoDB collection using pymongo. The topics are updated based on the
school's name provided to the function.
"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school name.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo
    collection object.
    name (str): The name of the school to update.
    topics (list): A list of strings representing topics to be set
    for the school.

    Returns:
    UpdateResult: The result of the update operation.
    """
    # Update the topics for the specified school
    result = mongo_collection.update_many(
        {"name": name},  # Match where name is equal to the provided name
        {"$set": {"topics": topics}}  # Set the new topics
    )

    return result
