from models.model import *
from models.monster import Monster
from utils.dbaccess import DbAccess

class RedisMonster:
    """
    モンスターのRedisアクセスクラス
    """
    def register(self, monster, tmp_flg = False):
        """
        モンスター登録処理

        Parameters
        ----------
        monster  : Monseter
        tmp_flg : boolean
            仮登録を行うかどうか
        """
        redis = DbAccess.get_connection_to_redis()
        pipe = redis.pipeline()

        team_monster_key = monster.get_team() + '-monster'

        if tmp_flg:
            monster_key = 'tmp-' + monster.get_team() + '-' + monster.get_name()
        else:
            monster_key =  monster.get_team() + '-' + monster.get_name()
            pipe.sadd(team_monster_key, monster_key)
        pipe.hset(monster_key, 'name', monster.get_name())
        pipe.hset(monster_key, 'team', monster.get_team())
        pipe.hset(monster_key, 'hp', monster.get_hp())
        pipe.hset(monster_key, 'power', monster.get_power())
        pipe.hset(monster_key, 'defence', monster.get_defence())
        pipe.hset(monster_key, 'attribute_cd', monster.get_attribute_cd())
        pipe.execute()

    def delete(self, key):
        """
        モンスターの削除処理

        Parameters
        ----------
        key : str
            モンスター識別キー
        """
        redis = DbAccess.get_connection_to_redis()
        redis.delete(key)

    def select(self, key):
        """
        モンスター取得処理
            キーで指定したモンスターを取得する

        Parameters
        ----------
        key : str
            モンスター識別キー

        Returns
        ----------
        Monsterクラス
        """
        redis = DbAccess.get_connection_to_redis()
        monster = redis.hgetall(key)
        return Monster(monster)

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
            monsters.append(Monster(monster))
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

        Returns
        ----------
        チーム集合 : set
        """
        redis = DbAccess.get_connection_to_redis()
        return redis.smembers('teams')
