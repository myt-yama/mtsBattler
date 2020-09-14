from models.model import *
from models.battle import Battle
from utils.dbaccess import DbAccess


class RedisBattle:
    def __init__(self, battle=None):
        if battle is None:
            battle = Battle()
        self.battle = battle
        self.redis = DbAccess.get_connection_to_redis()

    def fetch(self):
        battle_data = self.redis.hgetall(self.battle.battle_id)

        pipe = self.redis.pipeline()
        for player in range(1, battle_data['player_sum']+1):
            key = self._gen_monster_key(self.battle.battle_id, player)
            pipe.hgetall(key)
        monster_states = pipe.execute()

        self.battle.set_states(battle_data, monster_states)

    def save(self):
        pipe = self.redis.pipeline()

        battle_id = self.battle.battle_id
        # 登録
        # TODO:細かい修正
        pipe.hset(battle_id, 'player_sum', self.battle.player_sum])
        pipe.hset(battle_id, 'turn', self.battle.turn])
        for monster_state in self.battle.monster_states:
            for param in monster_state.get_monster_state_param():
                key = self._gen_monster_key(battle_id, monster_state.player)
                pipe.hset(key, param, getattr(monster_state, param))

        pipe.execute()

    def _gen_monster_key(self, battle_id, player):
        return str(battle_id)+'-'+str(player)

    def _convert_state_for_db(self):
        pass

    def _save(self, battle_state):
