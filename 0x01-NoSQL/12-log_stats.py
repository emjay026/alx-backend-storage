#!/usr/bin/env python3
"""
A script to provide statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs  # Access the 'logs' database
    collection = db.nginx  # Access the 'nginx' collection

    # Get the total number of documents in the collection
    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))

    # Define the methods we want to analyze
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        # Format output to match the exact requirement
        print("\tmethod {}: {}".format(method, method_count))

    # Count documents with method=GET and path=/status
    count_get_status = collection.count_documents({"method": "GET",
                                                   "path": "/status"})
    print("{} status check".format(count_get_status))


if __name__ == "__main__":
    main()
