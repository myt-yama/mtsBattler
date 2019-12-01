import sys
import os
import unittest
from unittest.mock import Mock

sys.path.append('../../')
sys.path.append('./')
from models.monster import Monster

class TestMonster(unittest.TestCase):
    def test_init(self):
        datas = [
            { "hp":     100, "power":    30, },
            { "hp": 1000000, "power": 50000, },
            { "hp":       0, "power":     0, },
            { "hp":     -10, "power":   -40, },
        ]
        expected = [
            { "hp":     100, "power":    30, },
            { "hp": 1000000, "power": 50000, },
            { "hp":       0, "power":     0, },
            { "hp":     -10, "power":   -40, },
        ]
        for i in range(len(datas)):
            t_monster = Monster(datas[i]["hp"], datas[i]["power"])
            self.assertEqual(t_monster.get_hp(), expected[i]['hp'])
            self.assertEqual(t_monster.get_power(), expected[i]['power'])

    def test_calculate_hp_after_attack(self):
        # 攻撃対象のモンスター設定
        attacked_monster = Monster(100, 0)
        datas = [
            { "hp": 100, "power":  30, },
            { "hp":   0, "power":   0, },
            { "hp":  10, "power": -40, },
        ]
        expected = [
            70,
            100,
            140,
        ]
        for i in range(len(datas)):
            t_monster = Monster(datas[i]["hp"], datas[i]["power"])
            rel_hp = t_monster.calculate_hp_after_attack(attacked_monster)
            self.assertEqual(rel_hp, expected[i])

if __name__ == '__main__':
    unittest.main()
