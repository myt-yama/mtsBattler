from models.model import *
from utils.dbaccess import DbAccess


class RedisTeam:
    """
    チームのRedisアクセスクラス
    """

    def __init__(self):
        self._redis = DbAccess.get_connection_to_redis()

    def register(self, team):
        """
        チーム登録処理

        Parameters
        ----------
        team : str
        """
        self._redis.sadd('teams', team)

    def fetch_all(self):
        """
        チーム取得処理
            全チームを取得する

        Returns
        ----------
        チーム集合 : set
        """
        return self._redis.smembers('teams')
