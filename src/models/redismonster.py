from models.model import *
from models.monster import Monster, MonsterList
from utils.dbaccess import DbAccess


class RedisMonster:
    """
    モンスターのRedisアクセスクラス
    """

    def __init__(self, monster=None):
        if monster is None:
            monster = Monster()
        self.monster = monster
        self.monster_list = MonsterList()
        self._redis = DbAccess.get_connection_to_redis()

    def register_tmp(self):
        pipe = self._redis.pipeline()
        monster_key = 'tmp-' + self.monster.team + '-' + self.monster.name
        self._register(monster_key, pipe)

    def register(self):
        """
        モンスター登録処理

        Parameters
        ----------
        monster  : Monseter
        tmp_flg : boolean
            仮登録を行うかどうか
        """
        pipe = self._redis.pipeline()

        monster_key = self.monster.team + '-' + self.monster.name
        team_monster_key = self.monster.team + '-monster'
        pipe.sadd(team_monster_key, monster_key)
        self._register(monster_key, pipe)

    def _register(self, key, pipe):

        pipe.hset(key, 'name', self.monster.name)
        pipe.hset(key, 'team', self.monster.team)
        pipe.hset(key, 'hp', self.monster.hp)
        # pipe.hset(key, 'power', monster.power)
        # pipe.hset(key, 'defence', monster.defence)
        # pipe.hset(key, 'attribute_cd', monster.attribute_cd)
        pipe.hset(key, 'image_path', self.monster.image_path)
        pipe.execute()

    def delete_tmp(self):
        self._delete('tmp-'+self.monster.id)

    def delete(self):
        """
        モンスターの削除処理

        Parameters
        ----------
        key : str
            モンスター識別キー
        """
        self._delete(self.monster.id)

    def _delete(self, key):
        self._redis.delete(key)

    def delete_all(self, key, team):
        """
        モンスター情報を全て削除する
            モンスターデータとチーム所属データ

        Parameters
        ----------
        key : str
            モンスター識別キー
        team : str
            チーム名
        """
        redis = DbAccess.get_connection_to_redis()
        pipe = redis.pipeline()
        pipe.delete(key)
        pipe.srem(team+'-monster', key)
        pipe.execute()

    def fetch_tmp(self):
        self._fetch('tmp-' + self.monster.id)

    def fetch(self, key):
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
        self._fetch(self.monster.id)

    def _fetch(self, key):
        params = self._redis.hgetall(key)
        self.monster.set_params(params)

    def fetch_all(self, team):
        """
        チームに所属する全モンスター取得処理

        Parameters
        ----------
        team : str
        """
        monster_keys = self._redis.smembers(team+'-monster')
        pipe = self._redis.pipeline()
        for key in monster_keys:
            pipe.hgetall(key)

        for monster in pipe.execute():
            monster['team'] = team
            self.monster_list.append_monster(Monster(monster))

        return self.monster_list.list if not self.monster_list.list == [] else None
