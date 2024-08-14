#!/usr/bin/env python3
"""Write strings to redis"""
import redis
import uuid
from typing import Union


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
