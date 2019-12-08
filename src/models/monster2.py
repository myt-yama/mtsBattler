from models import summon

class Monster:
    """
    モンスタークラス
    　モンスターのパラメータやメソッドを記述する

    Attributes
    ----------
    name : string
        名前
    hp    : int
        モンスターのHP
    power : int
        モンスターの攻撃力
    defence : int
        モンスターの防御力
    attribute : int
        属性
    """

    def __init__(self, name):
        """
        初期化メソッド
            各パラメータを設定する

        Parameters
        ----------
        name    : string
            名前
        """
        # TODO: 新しく生成 or DBから取得など複数の呼び出し方が考えられるため、
        #       クラス設計を練り直す必要あり。
        self.set_name(name)
        summoned_monster = summon.Summon(self)
        # summoned_monster.create_parameters(self)

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

    def set_name(self, name):
        self.__name = name

    def set_hp(self, hp):
        self.__hp = int(hp)

    def set_power(self, power):
        self.__power = int(power)

    def set_defence(self, defence):
        self.__defence = defence

    def set_attribute(self, attribute):
        self.__attribute = attribute

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_power(self):
        return self.__power

    def get_defence(self):
        return self.__defence

    def get_attribute(self):
        return self.__attribute

    def get_converted_attribute(self):
        """
        属性コードを属性名に変換して取得する

        Returns
        ----------
        string
            属性名
        """
        attribute = self.__attribute
        if attribute == 0:
            return '火'
        elif attribute == 1:
            return '水'
        elif attribute == 2:
            return '土'
        else:
            return '無'
