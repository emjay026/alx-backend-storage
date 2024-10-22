#!/usr/bin/env python3
"""
A module for handling student data in a MongoDB collection.

This module provides functionalities to insert student data,
list students, and retrieve top students sorted by their average score.
"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns a list of students sorted by average score.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo
    collection object to query.

    Returns:
    list: A list of dictionaries representing each student with
    their average score.

    Each returned student document includes the original information
    along with an 'averageScore' key that indicates the
    student's average score.
    """
    students_list = []

    # Retrieve all students from the collection
    students = mongo_collection.find()

    for student in students:
        # Calculate the average score
        topics = student.get('topics', [])
        if topics:
            average_score =\
                sum(topic.get('score', 0) for topic in topics) / len(topics)
            student['averageScore'] = average_score  # Add averageScore
            students_list.append(student)

    # Sort the list by averageScore in descending order
    students_list.sort(key=lambda x: x['averageScore'], reverse=True)

    return students_list
