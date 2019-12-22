from models.model import *
from models import summon2

class Monster:
    """
    モンスタークラス
    　モンスターのパラメータやメソッドを記述する

    Attributes
    ----------
    __key          : str
        キー（チーム名+名前）
    __name         : str
        名前
    __team         : str
        チーム名
    __hp           : int
        モンスターのHP
    __power        : int
        モンスターの攻撃力
    __defence      : int
        モンスターの防御力
    __attribute_cd : int
        属性コード
    __atribute     : str
        属性（属性コードを元に変換）
    """

    def __init__(self, parameters, summon_flg = False):
        """
        初期化メソッド
            各パラメータを設定する

        Parameters
        ----------
        paremeters : dict => {
                         # モンスターを生成する場合は name, teamが必須
                            name         : str
                           ,team         : str
                           ,hp           : int
                           ,power        : int
                           ,defence      : int
                           ,attribute_cd : str => "code, code, ..."
                        }
            モンスターの能力パラメータ
        summon_flg : boolean
            新たにパラメータを生成するかどうか
        """
        self.set_name(parameters['name'])
        self.set_team(parameters['team'])

        if summon_flg:
            summon2.Summon(self, summon_flg)
        else:
            self.set_hp(parameters['hp'])
            self.set_power(parameters['power'])
            self.set_defence(parameters['defence'])
            self.set_attribute_cd(parameters['attribute_cd'])
        self.set_attribute(''.join(list(map(lambda x: self.convert_from_attribute_cd(x), self.get_attribute_cd().split(',')))))

    def atack(self, target):
        """
        対象モンスターへの攻撃メソッド
        　対象モンスターのオブジェクトに攻撃後のHPを設定する

        Parameters
        ----------
        target : Monsterオブジェクト
            攻撃対象
        """
        rel_hp = self.calculate_hp_after_attack(target)
        target.set_hp(rel_hp)

    def calculate_hp_after_attack(self, target):
        """
        対象の攻撃後のHPを計算する

        Parameters
        ----------
        target : Monsterオブジェクト
            攻撃対象

        Returns
        ----------
        attacked_hp : int
            攻撃を受けた後の対象のHP
        """
        attacked_hp = target.get_hp() - self.get_power()
        return attacked_hp

    def set_team(self, team):
        self.team = team

    def set_name(self, name):
        self.name = name

    def set_hp(self, hp):
        self.hp = int(hp)

    def set_power(self, power):
        self.power = int(power)

    def set_defence(self, defence):
        self.defence = defence

    def set_attribute_cd(self, attribute_cd):
        self.attribute_cd = attribute_cd

    def set_attribute(self, attribute):
        self.attribute = attribute

    def get_team(self):
        return self.team

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_power(self):
        return self.power

    def get_defence(self):
        return self.defence

    def get_attribute_cd(self):
        return self.attribute_cd

    def convert_from_attribute_cd(self, code):
        if code == 0:
            return '火'
        elif code == 1:
            return '水'
        elif code == 2:
            return '土'
        else:
            return '無'
