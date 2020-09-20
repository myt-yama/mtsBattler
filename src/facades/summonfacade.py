from models.monster import Monster
from models.redismonster import RedisMonster
from models.redisteam import RedisTeam


class SummonFacade:
    def __init__(self, id=None):
        self.redis_team = RedisTeam()
        self.monster = Monster(id)
        self.redis_monster = RedisMonster(self.monster)

    def fetch_teams(self):
        return self.redis_team.fetch_all()

    def summon(self, team, name):
        self.monster.generate(team, name)
        self.redis_monster.register_tmp()
        return self.monster

    def register(self):
        self.redis_monster.fetch_tmp()
        self.redis_monster.delete_tmp()
        self.redis_monster.register()

    def register_cancel(self):
        self.redis_monster.delete_tmp()

    def delete(self, key, team):
        self.redis_monster.delete(key, team)
