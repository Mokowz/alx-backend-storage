#!/usr/bin/env python3
"""Write strings to redis"""
import redis
import sys
import uuid
from typing import Union, Callable, Optional


UnionMore = Union[str, bytes, int, float]


class Cache:
    "Store data in redis instance"
    def __init__(self):
        """Init function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionMore) -> str:
        """Store data in redis"""
        rand_key = str(uuid.uuid4())
        self._redis.mset({rand_key: data})
        return rand_key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> UnionMore:
        """COnvert to binary"""
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self: bytes) -> int:
        """Strings"""
        return int.from_bytes(self, sys.byteorder)

    def get_int(self: bytes) -> int:
        """Ints"""
        return self.decode("utf-8")
