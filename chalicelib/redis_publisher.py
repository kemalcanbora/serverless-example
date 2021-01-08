import redis
from functools import wraps
from .settings import REDIS_PASSWORD, REDIS_HOST
from json import dumps


def redis_connection():
    r = redis.Redis(host=REDIS_HOST,
                    password=REDIS_PASSWORD)
    return r


def publisher(channel):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            r = redis_connection()
            message = function(*args, **kwargs)
            r.publish(channel=channel,
                      message=dumps(message))
            return {"status": True}

        return wrapper

    return decorator
