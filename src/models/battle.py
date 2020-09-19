from models.model import *
from models.monsterstate import MonsterState


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

    def set_states(self, battle_state, monster_states):
        """
        バトル状況取得メソッド
        """
        self.turn = battle_state['turn']
        self.player_sum = battle_state['player_sum']

        for monster_state in monster_states:
            ms = MonsterState()
            ms.set_states(monster_state)
            self.monster_states.insert(int(monster_state['player']), ms)

    def set_monsters(self, monsters):
        self.player_sum = len(monsters)
        for i, monster in enumerate(monsters):
            ms = MonsterState()
            ms.set_monster(i+1, monster)
            self.monster_states.insert(i+1, ms)

    def set_commands(self, commands):
        self.commands = commands

    def fight(self):
        pass

    def _generate_battle_id(self):
        return 1000
