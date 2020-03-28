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
        'attribute_cd',
        'attribute',
        'charge',
    ]

    def __init__(self, battle_id=None, commands=None):
        """
        初期化メソッド
        """
        self.battle_id = battle_id
        self.commands = commands

    def select(self):
        """
        バトル状況取得メソッド
        """
        battle_status = redismodel.RedisBattle().select(self.battle_id)
        self.monster_number = int(battle_status['monster_number'])
        set_params_func = self._exec_func_to_battle_params(
            self._set_battle_param, self.monster_number)
        set_params_func(battle_status)

    def register(self):
        """
        バトル状況登録メソッド
        """
        battle_status = {
            'monster_number': self.monster_number,
        }
        get_params_func = self._exec_func_to_battle_params(
            self._get_battle_params, self.monster_number)
        params = get_params_func()
        battle_status.update(params)

        redismodel.RedisBattle().register(self.battle_id, battle_status)

    def set_monsters(self, monsters):
        self.monster_number = len(monsters)
        set_params_func = self._exec_func_to_battle_params(
            self._set_battle_param, self.monster_number)
        set_params_func(monsters)
        self.battle_id = 1000

    def get_parameter(self, player_number, parameter):
        return 'P' + str(player_number) + '_' + parameter

    def fight(self):
        pass

    def _exec_func_to_battle_params(self, func, total_monster_number):
        def inner(*args):
            result = {}
            for itr in range(total_monster_number):
                # DBへの登録対象となるパラメータをループで処理する
                for db_param in Battle.battle_parameters_in_db:
                    battle_param_name = self.get_parameter(itr+1, db_param)
                    func_args = (itr, db_param)+args
                    result[battle_param_name] = func(*func_args)
            return result
        return inner

    def _set_battle_param(self, itr, db_param, battle_params):
        player_number = itr+1
        battle_param_name = self.get_parameter(player_number, db_param)
        battle_param = self._get_battle_param_by_type(
            itr, battle_param_name, db_param, battle_params)

        setattr(self, battle_param_name, battle_param)

    def _get_battle_param_by_type(self, itr, battle_param_name, db_param, battle_params):
        if isinstance(battle_params, dict):
            return battle_params[battle_param_name]
        if isinstance(battle_params[itr], Monster):
            # Monsterクラスにないパラメータ, 初期値を設定する
            if db_param == "charge":
                return 0

            return getattr(battle_params[itr], db_param)

    def _get_battle_params(self, itr, db_param):
        player_number = itr+1
        battle_param_name = self.get_parameter(player_number, db_param)
        return getattr(self, battle_param_name)
