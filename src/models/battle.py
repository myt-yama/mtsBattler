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
    P1_team         : str
        P1_チーム名
    P1_name         : str
        P1_名前
    P1_hp           : int
        P1_HP
    P1_attribute_cd : str
        P1_属性
    P1_attribute    : str
        P1_属性
    P1_charge       : int
        P1_チャージ数
    P2_team         : str
        P2_チーム名
    P2_name         : str
        P2_名前
    P2_hp           : int
        P2_HP
    P2_attribute_cd : str
        P2_属性
    P2_attribute    : str
        P2_属性
    P2_charge       : int
        P2_チャージ数
    """

    def __init__(self, battle_id = None, commands = None):
        """
        初期化メソッド
        """
        self.battle_id = battle_id
        self.commands = commands.split(',') if commands is not None else None

    def select(self):
        """
        バトル状況取得メソッド
        """
        battle_status = redismodel.RedisBattle().select(self.battle_id)
        self.P1_team = battle_status['P1_team']
        self.P1_name = battle_status['P1_name']
        self.P1_hp = battle_status['P1_hp']
        self.P1_attribute_cd = battle_status['P1_attribute_cd']
        self.P1_attribute = battle_status['P1_attribute']
        self.P1_charge = battle_status['P1_charge']
        self.P2_team = battle_status['P2_team']
        self.P2_name = battle_status['P2_name']
        self.P2_hp = battle_status['P2_hp']
        self.P2_attribute_cd = battle_status['P2_attribute_cd']
        self.P2_attribute = battle_status['P2_attribute']
        self.P2_charge = battle_status['P2_charge']

    def register(self):
        """
        バトル状況登録メソッド
        """
        battle_status = {}
        battle_status['P1_team'] = self.P1_team
        battle_status['P1_name'] = self.P1_name
        battle_status['P1_hp'] = self.P1_hp
        battle_status['P1_attribute_cd'] = self.P1_attribute_cd
        battle_status['P1_attribute'] = self.P1_attribute
        battle_status['P1_charge'] = self.P1_charge
        battle_status['P2_team'] = self.P2_team
        battle_status['P2_name'] = self.P2_name
        battle_status['P2_hp'] = self.P2_hp
        battle_status['P2_attribute_cd'] = self.P2_attribute_cd
        battle_status['P2_attribute'] = self.P2_attribute
        battle_status['P2_charge'] = self.P2_charge
        redismodel.RedisBattle().register(self.battle_id, battle_status)

    def set_battle(self, battle_status):
        self.P1_team = battle_status['P1_team']
        self.P1_name = battle_status['P1_name']
        self.P1_hp = battle_status['P1_hp']
        self.P1_attribute_cd = battle_status['P1_attribute_cd']
        self.P1_attribute = battle_status['P1_attribute']
        self.P1_charge = battle_status['P1_charge']
        self.P2_team = battle_status['P2_team']
        self.P2_name = battle_status['P2_name']
        self.P2_hp = battle_status['P2_hp']
        self.P2_attribute_cd = battle_status['P2_attribute_cd']
        self.P2_attribute = battle_status['P2_attribute']
        self.P2_charge = battle_status['P2_charge']
        # TODO: 自動採番されるように変更
        self.battle_id = 1000

    def fight(self):
        pass
