#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps
""" A caching system with Redis"""


def count_calls(count_fn: Callable) -> Callable:
    """A decorator"""
    count = {}

    @wraps(count_fn)
    def wrapper(self, *args, **kwargs):
        func_name = count_fn.__qualname__
        count.setdefault(func_name, 0)
        count[func_name] += 1
        return count_fn(self, *args, **kwargs)
    return wrapper


class Cache:
    """ Class cache"""
    def __init__(self, host='localhost', port=6379, db=0):
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn : Optional[Callable] = None):
        data = self._redis.get(key)
        if data is not None:
            if fn:
                return fn(data)
            else:
                return data
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, lambda data: data.decode("utf-8"))

    def get_int(self, key: str) -> int:
        return self.get(key, lambda data: int(data.decode("utf-8")))
