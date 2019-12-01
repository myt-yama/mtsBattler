class Monster:
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
        self.set_hp(hp)
        self.set_power(power)

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

    def set_hp(self, hp):
        self.__hp = int(hp)

    def set_power(self, power):
        self.__power = int(power)

    def get_hp(self):
        return self.__hp

    def get_power(self):
        return self.__power

