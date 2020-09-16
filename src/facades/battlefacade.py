from models.model import *
from models.battle import Battle
from models.redisbattle import RedisBattle


class BattleFacade:
    def __init__(self, battle_id=None):
        self.battle = Battle(battle_id)
        self.redis_battle = RedisBattle(self.battle)

    def ready(self, monsters):
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
