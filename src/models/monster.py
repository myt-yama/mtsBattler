from models.model import *
from models.summon import Summon


class Monster:
    """
    モンスタークラス
        モンスターのパラメータやメソッドを記述する

    Attributes
    ----------
    id           : str
        ID(team+name)
    name         : str
        名前
    team         : str
        チーム名
    hp           : int
        モンスターのHP
    power        : int
        モンスターの攻撃力
    defence      : int
        モンスターの防御力
    attribute_cd : int
        属性コード
    atribute     : str
        属性（属性コードを元に変換）
    image_path   : 画像ファイル
    """

    def __init__(self, id=None):
        """
        初期化メソッド
            各パラメータを設定する

        Parameters
        ----------
        id : str
            ID(team+name)
        """
        self.id = id
        self.summon = Summon(self)

    def set_params(self, params):
        """
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
                           ,image_path   : str
                        }
            モンスターの能力パラメータ
        """
        self.name = params['name']
        self.team = params['team']
        self.hp = params['hp']
        self.image_path = params['image_path']
        # self.power = params['power']
        # self.defence = params['defence']
        # self.attribute_cd = params['attribute_cd']

    def generate(self, team, name):
        self.team = team
        self.name = name
        self.summon.generate_parameters_by_name(name)


class MonsterList:
    def __init__(self):
        self.list = []

    def append_monster(self, monster):
        self.list.append(monster)
