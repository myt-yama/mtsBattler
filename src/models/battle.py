from models.model import *
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

    def __init__(self, battle_id = None, commands = None):
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
        for i in range(self.monster_number):
            # propetyに使用する番号, iは0始まりのため1足す
            player_number = i+1
            for parameter in Battle.battle_parameters_in_db:
                battle_parameter = self.get_parameter(player_number, parameter)
                setattr(self, battle_parameter, battle_status[battle_parameter])

    def register(self):
        """
        バトル状況登録メソッド
        """
        battle_status = {
            'monster_number' : self.monster_number,
        }
        for i in range(self.monster_number):
            player_number = i+1
            for parameter in Battle.battle_parameters_in_db:
                battle_parameter = self.get_parameter(player_number, parameter)
                battle_status[battle_parameter] = getattr(self, battle_parameter)
        redismodel.RedisBattle().register(self.battle_id, battle_status)

    def set_monsters(self, monsters):
        self.monster_number = len(monsters)
        for i in range(self.monster_number):
            # propetyに使用する番号, iは0始まりのため1足す
            player_number = i+1
            monster = monsters[i]
            for parameter in Battle.battle_parameters_in_db:
                battle_parameter = self.get_parameter(player_number, parameter)
                if parameter != 'charge':
                    setattr(self, battle_parameter, getattr(monster, parameter))
                else:
                    # Monsterクラスにないパラメータ, 初期値を設定する
                    setattr(self, battle_parameter, 0)
        # TODO: 自動採番されるように変更
        self.battle_id = 1000

    def get_parameter(self, player_number, parameter):
        return 'P'+str(player_number)+'_'+parameter

    def fight(self):
        pass
