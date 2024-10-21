#!/usr/bin/env python3
"""
This module provides a function to list all documents in a MongoDB collection
using pymongo. It connects to a specified MongoDB collection and can return
the documents stored within that collection.
"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in the specified MongoDB collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection):
    The pymongo collection object.

    Returns:
    list: A list containing all documents in the collection
    or an empty list if there are none.
    """
    # Retrieve all documents from the collection
    documents = list(mongo_collection.find())

    return documents
