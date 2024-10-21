#!/usr/bin/env python3
"""
This module provides a function to insert a new
document into a MongoDB collectionusing pymongo.
The document is created using keyword
arguments passed to the function.
"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the specified MongoDB collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection):
    The pymongo collection object.
    **kwargs: Fields and values to be included in the new document.

    Returns:
    ObjectId: The _id of the newly inserted document.
    """
    # Insert the document into the collection
    result = mongo_collection.insert_one(kwargs)

    # Return the new document's _id
    return result.inserted_id
