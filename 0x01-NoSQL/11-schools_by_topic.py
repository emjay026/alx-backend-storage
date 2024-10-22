#!/usr/bin/env python3
"""
A module for retrieving school information based on topics.

This module provides a function to query a MongoDB collection
and return a list of schools that have a specified topic.
"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve a list of schools associated with a given topic.

    Parameters:
    mongo_collection (pymongo.collection.Collection):
    The pymongo collection object to query.
    topic (str): The topic to search for in school records.

    Returns:
    list: A list of school documents that have the specified topic.

    Each document includes the school's ID, name, and topics.
    """
    # Query the collection for documents that contain the specified topic
    schools = mongo_collection.find({"topics": topic})

    # Create a list of school documents
    school_list = list(schools)  # Convert cursor to a list

    return school_list
