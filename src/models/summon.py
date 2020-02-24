from models.model import *
import re
import urllib.request
import json
import math

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
        status_points = self.generate_status_points(base_value)
        percentages = self.decide_percentage(base_value)
        kanji = self._select_kanji(name)

        self.assign_image(base_value)
        self.assign_points_to_status(status_points, percentages)
        self.generate_attribute(kanji)

    def generate_status_points(self, value):
        points = 140 + (value % 20)

        return points

    def decide_percentage(self, value):
        select = []
        for i in range(3):
            for j in range(4):
                select.append(j)
        patterns = [
            [0.2,0.2,0.6],
            [0.2,0.3,0.5],
            [0.2,0.4,0.4],
            [0.3,0.3,0.4],
        ]
        table = patterns[select[int(str(value)[round(len(str(value))/2)])]]

        percentages = []
        if value%6 == 0:
            percentages.append(table[0])
            percentages.append(table[1])
            percentages.append(table[2])
        elif value%6 == 1:
            percentages.append(table[0])
            percentages.append(table[2])
            percentages.append(table[1])
        elif value%6 == 2:
            percentages.append(table[1])
            percentages.append(table[0])
            percentages.append(table[2])
        elif value%6 == 3:
            percentages.append(table[1])
            percentages.append(table[2])
            percentages.append(table[0])
        elif value%6 == 4:
            percentages.append(table[2])
            percentages.append(table[0])
            percentages.append(table[1])
        elif value%6 == 5:
            percentages.append(table[2])
            percentages.append(table[1])
            percentages.append(table[0])

        return percentages



    def assign_points_to_status(self, points, percentages):
        hp = math.floor((50 + points * percentages[0]) * 5)
        power = math.floor(50 + points * percentages[1])
        defence = math.floor(50 + points * percentages[2])

        self.monster.set_hp(hp)
        self.monster.set_power(power)
        self.monster.set_defence(defence)

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

    def assign_image(self, value):
        if value % 2 == 0:
            self.monster.image_path = '/static/img/blue_monster.png'
        else:
            self.monster.image_path = '/static/img/green_monster.png'

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
        # TODO:redisから取得する
        fire  = { i*3 for i in range(70) }
        water = { i*7 for i in range(30) }
        grass = { i*5 for i in range(42) }

        ret = []
        if len(bushu_codes)>0:
            bushu_codes_set = set(bushu_codes)
            if len(fire & bushu_codes_set) > 0:
                ret.append('1')
            if len(water & bushu_codes_set) > 0:
                ret.append('2')
            if len(grass & bushu_codes_set) > 0:
                ret.append('3')
        if len(ret) == 0:
            ret.append('3')

        return ",".join(ret)

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
