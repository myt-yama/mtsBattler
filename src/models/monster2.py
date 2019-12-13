from models import summon

class Monster:
    """
    モンスタークラス
    　モンスターのパラメータやメソッドを記述する

    Attributes
    ----------
    __name         : str
        名前
    __id           : int
        モンスターのID
    __hp           : int
        モンスターのHP
    __power        : int
        モンスターの攻撃力
    __defence      : int
        モンスターの防御力
    __attribute_cd : int
        属性コード
    """

    def __init__(self, parameters, summon_flg = True):
        """
        初期化メソッド
            各パラメータを設定する

        Parameters
        ----------
        paremeters : dict => {
                          # 必須項目
                            name         : string

                          # 新規生成の場合は以下不要 
                          # id はDB登録時に割り振られるため、新規生成以外でも必ずしも設定する必要はない
                           ,id           : Int
                           ,hp           : Int
                           ,power        : Int
                           ,defence      : Int
                           ,attribute_cd : Int
                        }
            モンスターの能力パラメータ
        summon_flg : boolean
            新たにパラメータを生成するかどうか
        """
        self.set_name(parameters['name'])
        # 値がない場合は None を設定する 
        self.set_id(parameters.get('id'))

        if summon_flg:
            summon.Summon(self)
        else:
            self.set_power(parameters['power'])
            self.set_defence(parameters['defence'])
            self.set_attribute_cd(parameters['attribute_cd'])

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
        return self.__attribute_cd

    def get_converted_attribute(self):
        """
        属性コードを属性名に変換して取得する

        Returns
        ----------
        string
            属性名
        """
        attribute = self.__attribute_cd
        if attribute == 0:
            return '火'
        elif attribute == 1:
            return '水'
        elif attribute == 2:
            return '土'
        else:
            return '無'
