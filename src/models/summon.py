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
        パラメータの元となる値を設定する

        Parameters
        ----------
        monster : Monsterクラス
        """
        base_value = monster.get_name()
        monster.set_hp(self.generate_hp(base_value))
        monster.set_power(self.generate_power(base_value))
        monster.set_defence(self.generate_defence(base_value))

        kanji = self._select_kanji(base_value)
        monster.set_attribute(self.generate_attribute(kanji))

    def generate_hp(self, val):
        return 100

    def generate_power(self, val):
        return 30

    def generate_defence(self, val):
        return 20

    def generate_attribute(self, kanji):
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
        if len(bushu_codes)>0:
            if bushu_codes[0] > 50:
                return 0
            else:
                return 1
        else:
            return 2

    def _select_bushu_codes(self, kanji):
        bushu_codes = []
        for character in list(kanji):
            bushu_codes.append(self._get_bushu(character))
        return bushu_codes

    def _get_bushu(self, character):
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
