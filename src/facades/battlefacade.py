from models.model import *
from models.battle import Battle
from models.redisbattle import RedisBattle
from models.redismonster import RedisMonster


class BattleFacade:
    def __init__(self, battle_id=None):
        self.battle = Battle(battle_id)
        self.redis_battle = RedisBattle(self.battle)

    def ready(self, monster_ids):
        monsters = []
        for id in monster_ids:
            monsters.append(self._fetch_monster(id))
        self.battle.set_monsters(monsters)
        self.redis_battle.save()

        return self.battle

    def fight(self, commands):
        self.redis_battle.fetch()

        # TODO: バトルロジック作成
        self.battle.set_commands(commands)
        self.battle.fight()
        self.redis_battle.save()
        # logging.info(battle.commands)

        return self.battle

    def _fetch_monster(self, id):
        redis_monster = RedisMonster()
        redis_monster.fetch(id)
        return redis_monster.monster
