from abc import ABCMeta
from utils.dbaccess import DbAccess
from models import monster2

class RedisModel(object, metaclass=ABCMeta):
    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def select(self):
        pass

class RedisMonster(RedisModel):
    def register(self, monster):
        redis = DbAccess.get_connection_to_redis()
        pipe = redis.pipeline()

        team_monster_key = monster.get_team() + '-monster'
        monster_key = monster.get_team() + '-' + monster.get_name()
        pipe.sadd(team_monster_key, monster_key)
        pipe.hset(monster_key, 'name', monster.get_name())
        pipe.hset(monster_key, 'hp', monster.get_hp())
        pipe.hset(monster_key, 'power', monster.get_power())
        pipe.hset(monster_key, 'defence', monster.get_defence())
        pipe.hset(monster_key, 'attribute', monster.get_attribute_cd())
        pipe.execute()

    def select(self, key):
        redis = DbAccess.get_connection_to_redis()
        monster = redis.hgetall(key)
        return monster2.Monster(monster)

    def select_all(self, team):
        redis = DbAccess.get_connection_to_redis()
        monster_keys = redis.smembers(team)
        pipe = redis.pipeline()
        for key in monster_keys:
            p.hgetall(key)
        monsters = []
        for monster in p.execute():
            monster['attribute'] = ''.join(list(map(lambda x: convert_attribute_cd(x), monster['attribute'].split(','))))
            monsters.append(monster)
        return monsters

class RedisTeams(RedisModel):

    def register(self, team):
        redis = DbAccess.get_connection_to_redis()
        redis.sadd('teams', team)

    def select(self):
        redis = DbAccess.get_connection_to_redis()
        return redis.smembers('teams')
