import redis
from config import REDIS_URL


redis_client = redis.from_url(REDIS_URL, decode_responses=True)


def get_cache(key: str):
    return redis_client.get(key)


def set_cache(key: str, value: str, ttl: int = 60):
    redis_client.set(key, value, ex=ttl)


def delete_cache(key: str):
    redis_client.delete(key)
