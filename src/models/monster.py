class Monster():
    """
    モンスタークラス
    　モンスターのパラメータやメソッドを記述する

    Attributes
    ----------
    hp    : int
        モンスターのHP
    power : int
        モンスターの攻撃力
    """

    def __init__(self, hp, power):
        """
        初期化メソッド
        　HPと攻撃力を設定する

        Parameters
        ----------
        hp    : int
            モンスターのHP
        power : int
            モンスターの攻撃力
        """
        self.__hp = hp
        self.__power = power

    def atack(self, target):
        """
        対象モンスターへの攻撃メソッド
        　対象モンスターのオブジェクトに攻撃後のHPを設定する

        Parameters
        ----------
        target : Monsterオブジェクト
        """
        rel_hp = target.get_hp() - self.get_power()
        target.set_hp(rel_hp)

    def set_hp(self, hp):
        self.__hp = hp

    def get_hp(self):
        return self.__hp

    def get_power(self):
        return self.__power

