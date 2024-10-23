#!/usr/bin/env python3

"""
This module provides a simple caching class that utilizes
Redis for storage.
The Cache class allows for storing various types of data
(string, bytes, int, float)
with a unique key generated using UUID.
"""

import redis
import uuid
from typing import Union


class Cache:
    """A simple caching class that uses Redis for storage."""

    def __init__(self) -> None:
        """Initializes the Cache with a Redis client and
        flushes the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis and returns the generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to
            store in the cache.

        Returns:
            str: A unique key associated with the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
