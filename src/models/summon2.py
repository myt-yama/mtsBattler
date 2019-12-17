import re
import urllib.request
import json

import logging
logging.basicConfig(level=logging.DEBUG)

class Summon:
    """
    モンスター生成クラス
    　モンスターのパラメータを生成する
    """
    def __init__(self, monster, summon_flg = False):
        """
        パラメータを生成する

        Parameters
        ----------
        monster    : Monster
        summon_flg : boolean
        """
        self.monster = monster
        if summon_flg:
            self.genereate_parameters_by_name(monster.get_name())

    def genereate_parameters_by_name(self, name):
        """
        名前を元にすべてのパラメータを生成しセットする

        Parameters
        ----------
        name : str
            モンスター生成の元データ
        """
        base_value = self._convert_string_to_int(name)
        kanji = self._select_kanji(name)

        self.generate_hp(base_value),
        self.generate_power(base_value),
        self.generate_defence(base_value),
        self.generate_attribute(kanji),

    def generate_hp(self, value):
        """
        HPを生成する

        Parameters
        ----------
        value : int
            パラメータ生成の元となる値
        """
        # TODO: ロジック作る
        base_hp = 70
        mod = value % 60
        result = base_hp+mod

        self.monster.set_hp(result)

    def generate_power(self, value):
        """
        攻撃力を計算する

        Parameters
        ----------
        value : int
            パラメータ生成の元となる値
        """
        # TODO: ロジック作る
        base_power = 10
        mod = value % 10
        result = base_power+mod

        self.monster.set_power(result)

    def generate_defence(self, value):
        """
        防御力を計算する

        Parameters
        ----------
        value : int
            パラメータ生成の元となる値
        """
        # TODO: ロジック作る
        base_defence = 10
        mod = value % 5
        result =  base_defence+mod
        self.monster.set_defence(result)

    def generate_attribute(self, kanji):
        """
        属性を判定する

        Parameters
        ----------
        kanji : string
            漢字の羅列
        """
        # TODO: ロジック作る
        bushu_codes = self._select_bushu_codes(kanji)
        self.monster.set_attribute_cd(self._judge_attribute(bushu_codes))

    def _select_kanji(self, value):
        """
        漢字を抽出する

        Parameters
        ----------
        value : string
            漢字を含む文字列

        Returns
        ----------
        kanji : string
            漢字のみ
        """
        kanji_regex = re.compile('[\u2E80-\u2FDF\u3005-\u3007\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002EBEF]+')
        kanji = ''.join(kanji_regex.findall(value))
        return kanji

    def _judge_attribute(self, bushu_codes):
        """
        属性判定ロジック

        Parameters
        ----------
        bushu_codes : list[int,int,...]
            部首コードのリスト

        Returns
        ----------
        int
            属性コード
        """
        if len(bushu_codes)>0:
            if bushu_codes[0] > 50:
                return '0'
            else:
                return '1'
        else:
            return '2'

    def _select_bushu_codes(self, kanji):
        """
        各漢字から部首コードの取得する

        Parameters
        ----------
        kanji : string
            漢字の羅列

        Returns
        ----------
        bushu_codes : list[int,int,...]
            部首コードのリスト
        """
        bushu_codes = []
        for character in list(kanji):
            bushu_codes.append(self._get_bushu(character))
        return bushu_codes

    def _get_bushu(self, character):
        """
        MJ文字情報検索システムのAPIを使用し、部首コードを取得する

        Parameters
        ----------
        kanji : string
            漢字一文字

        Returns
        ----------
        int
            部首コード
        """
        # convert character to hex unicode
        letter_a = str(character)
        decimal_a = ord(letter_a)
        hex_A = hex(decimal_a)

        # insert into api request format
        request_url = "http://mojikiban.ipa.go.jp/mji/q?UCS=*"
        request_url = request_url.replace('*', hex_A)

        req = urllib.request.Request(request_url)

        with urllib.request.urlopen(req) as res:
            body = json.load(res)

        return body['results'][0]['部首内画数'][0]['部首']

    def _convert_string_to_int(self, val):
        """
        文字列をintへ変換する
        　文字列 -> 16進数 -> 10進数

        Parameters
        ----------
        val : string
            変換対象の文字列

        Returns : int
            10進数に変換した値
        """
        return int(val.encode('utf-8').hex(), 16)

    def get_monster(self):
        return self.monster
