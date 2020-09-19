from models.redismonster import RedisMonster


class FarmFacade:
    def __init__(self):
        self.monsters = []
        self.redis_monster = RedisMonster()
        # self.redis_monster = RedisMonster(self.monster)

    def fetch_monsters(self, team):
        self.monsters = self.redis_monster.fetch_all(team)
