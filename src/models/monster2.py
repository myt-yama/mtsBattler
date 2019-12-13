from models import summon

class Monster:
    """
    モンスタークラス
    　モンスターのパラメータやメソッドを記述する

    Attributes
    ----------
    __name         : String
        名前
    __id           : Int
        モンスターID
    __hp           : Int
        モンスターのHP
    __power        : Int
        モンスターの攻撃力
    __defence      : Int
        モンスターの防御力
    __attribute_cd : Int
        属性コード
    """

    def __init__(self, name=None :: String, id=None :: Int, hp=None :: Int, power=None :: Int, defence=None :: Int, attribute_cd=None :: Int):
        """
        初期化メソッド
            各パラメータを設定する

        Parameters
        ----------
        name         : string
        id           : Int
        hp           : Int
        power        : Int
        defence      : Int
        attribute_cd : Int
        """
        # TODO: 新しく生成 or DBから取得など複数の呼び出し方が考えられるため、
        #       クラス設計を練り直す必要あり。
        self.set_name(name)
        self.set_id(id)

        if id == None:
            summon.Summon(self)
        else:
            self.set_power(power)
            self.set_defence(defence)
            self.set_attribute_cd(attribute_cd)

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

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_hp(self, hp):
        self.__hp = int(hp)

    def set_power(self, power):
        self.__power = int(power)

    def set_defence(self, defence):
        self.__defence = defence

    def set_attribute_cd(self, attribute_cd):
        self.__attribute_cd = attribute_cd

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
