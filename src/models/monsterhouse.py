from models import monster2

import logging
logging.basicConfig(level=logging.DEBUG)

class MonsterHouse:
    """
    DBとのインターフェース

    Attributes
    ----------
    monster : Monster
        モンスターオブジェクト
    """
    def __init__(self, monster :: Monster):
        """
        初期化メソッド
            モンスターオブジェクトをセットする
        """
        self.monster = monster

    def register_db(self):
        """
        DBへ登録する
        """
        pass

    def get_from_db(self):
        """
        DBから取得する
        """
        pass