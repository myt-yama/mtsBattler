import redis

class DbAccess:
    @staticmethod
    def get_connection_to_redis():
        return redis.Redis(host='redis', port=6379, db=0, decode_responses=True)
