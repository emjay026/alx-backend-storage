#!/usr/bin/env python3

"""
This module provides a function to retrieve the HTML content of a given URL
while tracking the number of times that URL has been accessed and caching
the results.
"""

import requests
import redis
from functools import wraps

# Initialize Redis client (make sure Redis is running locally)
cache = redis.Redis()


def cache_page(expiration: int = 10):
    """Decorator to cache the result of get_page function."""

    def decorator(func):
        @wraps(func)
        def wrapper(url: str) -> str:
            # Check if the result is cached
            cached_result = cache.get(url)
            if cached_result:
                # Return cached result if available
                return cached_result.decode('utf-8')

            # Call the original function
            result = func(url)
            # Cache the result with an expiration time
            cache.setex(url, expiration, result)
            return result

        return wrapper

    return decorator


@cache_page(expiration=10)
def get_page(url: str) -> str:
    """Fetches the HTML content from the given URL.

    Args:
        url (str): The URL of the page to retrieve.

    Returns:
        str: The HTML content of the page.
    """
    # Track the access count for the URL
    cache.incr(f"count:{url}")
    response = requests.get(url)
    return response.text
