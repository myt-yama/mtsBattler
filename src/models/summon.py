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
    def __init__(self, monster):
        """
        パラメータを設定する

        Parameters
        ----------
        monster : Monsterクラス
        """
        # パラメータ計算の元となる値を取得
        base_value = self._convert_string_to_int(monster.get_name())
        monster.set_hp(self.generate_hp(base_value))
        monster.set_power(self.generate_power(base_value))
        monster.set_defence(self.generate_defence(base_value))

        # 属性だけは名前に含まれる漢字を使う
        kanji = self._select_kanji(monster.get_name())
        monster.set_attribute(self.generate_attribute(kanji))

    def generate_hp(self, val):
        """
        HPを生成する

        Parameters
        ----------
        val : int
            パラメータ生成の元となる値

        Returns
        ----------
        int
            算出したHPの値
        """
        # TODO: ロジック作る
        base_hp = 70
        mod = val % 60
        return base_hp+mod

    def generate_power(self, val):
        """
        攻撃力を計算する

        Parameters
        ----------
        val : int
            パラメータ生成の元となる値

        Returns
        ----------
        int
            算出した攻撃力の値
        """
        # TODO: ロジック作る
        base_power = 10
        mod = val % 10
        return base_power+mod

    def generate_defence(self, val):
        """
        防御力を計算する

        Parameters
        ----------
        val : int
            パラメータ生成の元となる値

        Returns
        ----------
        int
            算出した防御力の値
        """
        # TODO: ロジック作る
        base_defence = 10
        mod = val % 5
        return base_defence+mod

    def generate_attribute(self, kanji):
        """
        属性を判定する

        Parameters
        ----------
        kanji : string
            漢字の羅列

        Returns
        ----------
        int
            属性コード
        """
        # TODO: ロジック作る
        bushu_codes = self._select_bushu_codes(kanji)
        return self._judge_attribute(bushu_codes)

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
                return 0
            else:
                return 1
        else:
            return 2

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
