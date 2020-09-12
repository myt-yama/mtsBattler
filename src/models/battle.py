from models.model import *
from models.monster import Monster
from models import redismodel


class Battle:
    """
    バトルクラス

    Attributes
    ----------
    battle_id       : int
        バトルID
    commands        : str => P1_コマンド,P2_コマンド
        コマンド
    monster_number  : int
        参加モンスター数
    _is_set_monster  : bool
        モンスターがセットされてるか
    Px_team         : str
        Px_チーム名
    Px_name         : str
        Px_名前
    Px_hp           : int
        Px_HP
    Px_attribute_cd : str
        Px_属性
    Px_attribute    : str
        Px_属性
    Px_charge       : int
        Px_チャージ数
    """
    battle_parameters_in_db = [
        'team',
        'name',
        'hp',
        # 'attribute_cd',
        # 'attribute',
        'charge',
    ]

    def __init__(self, battle_id=None):
        """
        初期化メソッド
            バトル開始（battle_idがない場合）はbattle_idを発行する
            バトル中はbattle_idをセットする
        """
        if battle_id is None:
            battle_id = self._generate_battle_id()
        self.battle_id = battle_id
        self._is_set_monster = false

    def fetch_situation(self):
        """
        バトル状況取得メソッド
        """
        # TODO: データ取得処理修正
        monsters_state = redismodel.RedisBattle().select(self.battle_id)

        self.monster_number = len(monsters_state)
        for state in monsters_state:
            self._set_state(state)
        self._is_set_monster = True

    def _set_state(state):
        player = state[player]
        for db_param in Battle.battle_parameters_in_db:
            param = self.get_parameter(player, db_param)
            setattr(self, param, state[db_param])


    def register(self):
        """
        バトル状況登録メソッド
        """
        # モンスターがセットされてるかチェック
        if not self._is_set_monster:
            # TODO: 例外処理
            logging.err("モンスターがセットされていません")
            return False

        # DB登録用にデータを加工
        situation = self._convert_situation_for_db()

        # 登録
        redismodel.RedisBattle().register(self.battle_id, situation)

    def _convert_situation_for_db():
        pass


    def set_monsters(self, monsters):
        self.monster_number = len(monsters)
        for i, monster in enumerate(monsters):
            self._set_state(self._convert_monster_to_state(i ,monster))
        self._is_set_monster = True

    def _convert_monster_to_state(self, player, monster):
        state = []
        state['player'] = player
        state['charge'] = 0
        for db_param in Battle.battle_parameters_in_db:
            state[db_param] = getattr(monster, db_param)

        return state

    def get_parameter(self, player_number, parameter):
        return 'P' + str(player_number) + '_' + parameter

    def fight(self):
        pass

