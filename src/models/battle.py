from models.model import *
from models.monster import Monster
from models.monsterstate import MonsterState
from models import redismodel


class Battle:
    """
    バトルクラス

    Attributes
    ----------
    battle_id   : int
        バトルID
    commands    : list[int]
        コマンド
    player_sum  : int
        参加プレイヤー数
    monster_states    : list[MonsterState]
        モンスターリスト
    turn        : int
        経過ターン数
    """

    def __init__(self, battle_id=None):
        """
        初期化メソッド
            バトル開始（battle_idがない場合）はbattle_idを発行する
            バトル中はbattle_idをセットする
        """
        if battle_id is None:
            battle_id = self._generate_battle_id()
        self.battle_id = battle_id
        self.turn = 0
        self.monster_states = []

    def set_battle_state(self, battle_state, monster_states):
        """
        バトル状況取得メソッド
        """
        self.turn = battle_state['turn']
        self.player_sum = battle_state['player_sum']

        #TODO: 共通化
        for monster_state in monster_states:
            ms = MonsterState()
            ms.set_monster_state(monster_state)
            self.monster_states.insert(i+1, ms)

    def set_monster_states(self, monsters):
        #TODO: 共通化
        self.player_sum = len(monsters)
        for i, monster in enumerate(monsters):
            ms = MonsterState()
            ms.set_battle_monster(i+1, monster)
            self.monster_states.insert(i+1, ms)
    def set_commands(self, commands):
        self.commands = commands

    def fight(self):
        pass
