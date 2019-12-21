from utils.dbaccess import DbAccess
from models import monster2

import logging
logging.basicConfig(level=logging.DEBUG)

class RedisMonster:
    """
    モンスターのRedisアクセスクラス
    """
    def register(self, monster):
        """
        モンスター登録処理

        Parameters
        ----------
        monster : Monseter
        """
        redis = DbAccess.get_connection_to_redis()
        pipe = redis.pipeline()

        team_monster_key = monster.get_team() + '-monster'
        monster_key = monster.get_team() + '-' + monster.get_name()
        pipe.sadd(team_monster_key, monster_key)
        pipe.hset(monster_key, 'name', monster.get_name())
        pipe.hset(monster_key, 'hp', monster.get_hp())
        pipe.hset(monster_key, 'power', monster.get_power())
        pipe.hset(monster_key, 'defence', monster.get_defence())
        pipe.hset(monster_key, 'attribute_cd', monster.get_attribute_cd())
        pipe.execute()

    def select(self, key):
        """
        モンスター取得処理
            キーで指定したモンスターを取得する

        Parameters
        ----------
        key : str
            チーム名+モンスター名

        Returns
        ----------
        Monsterクラス
        """
        redis = DbAccess.get_connection_to_redis()
        monster = redis.hgetall(key)
        return monster2.Monster(monster)

    def select_all(self, team):
        """
        チームに所属する全モンスター取得処理

        Parameters
        ----------
        team : str
        """
        redis = DbAccess.get_connection_to_redis()
        monster_keys = redis.smembers(team+'-monster')
        pipe = redis.pipeline()
        for key in monster_keys:
            pipe.hgetall(key)
        monsters = []
        for monster in pipe.execute():
            monster['team'] = team
            monsters.append(monster2.Monster(monster))
        return monsters

class RedisTeams:
    """
    チームのRedisアクセスクラス
    """
    def register(self, team):
        """
        チーム登録処理

        Parameters
        ----------
        team : str
        """
        redis = DbAccess.get_connection_to_redis()
        redis.sadd('teams', team)

    def select(self):
        """
        チーム取得処理
            全チームを取得する
        """
        redis = DbAccess.get_connection_to_redis()
        return redis.smembers('teams')
