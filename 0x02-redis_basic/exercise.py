#!/usr/bin/env python3

"""
This module provides a simple caching class
that utilizes Redis for storage.
The Cache class allows for storing various
types of data (string, bytes, int, float)
with a unique key generated using UUID and
provides methods to retrieve the stored
data with automatic conversion.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count calls to methods and track
    they are stored in Redis."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Increment the call count for this method in Redis
        key = method.__qualname__
        self._redis.incr(key)  # Increment call count in Redis
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to track the history of inputs
    and outputs for a function."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Create input and output list keys
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Normalize input arguments to a string and
        # push to inputs in Redis
        self._redis.rpush(input_key, str(args))

        # Execute the original method and get the output
        output = method(self, *args, **kwargs)

        # Push the output to outputs list in Redis
        self._redis.rpush(output_key, str(output))

        return output

    return wrapper


def replay(method: Callable) -> None:
    """Displays the history of calls to a particular function."""
    # Retrieve the qualified name of the method
    method_name = method.__qualname__

    # Get input and output history from Redis
    inputs = method.__self._redis.lrange(f"{method_name}:inputs", 0, -1)
    outputs = method.__self._redis.lrange(f"{method_name}:outputs", 0, -1)

    # Count the number of calls
    call_count = len(inputs)

    # Print the replay information
    print(f"{method_name} was called {call_count} times:")

    # Pair inputs with outputs and display them
    for input_data, output_data in zip(inputs, outputs):
        print(f"{method_name}(*{input_data.decode()})"
              f"-> {output_data.decode()}")


class Cache:
    """A simple caching class that uses Redis for storage."""

    def __init__(self) -> None:
        """Initializes the Cache with a Redis client
        and flushes the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis and returns the generated key.

        Args:
            data (Union[str, bytes, int, float]):
            The data to store in the cache.

        Returns:
            str: A unique key associated with the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Optional[Union[str, bytes, int, float]]:
        """Retrieves data from Redis and applies an optional
        conversion function.

        Args:
            key (str): The key to retrieve the data for.
            fn (Optional[Callable]): A function to convert the
            data back to the desired format.

        Returns:
            Optional[Union[str, bytes, int, float]]: The retrieved
            and converted data, or None if the key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """Retrieves data as a UTF-8 string.

        Args:
            key (str): The key to retrieve the data for.

        Returns:
            Optional[str]: The retrieved data as a UTF-8 string,
            or None if the key does not exist.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieves data as an integer.

        Args:
            key (str): The key to retrieve the data for.

        Returns:
            Optional[int]: The retrieved data as an integer,
            or None if the key does not exist.
        """
        return self.get(key, int)
