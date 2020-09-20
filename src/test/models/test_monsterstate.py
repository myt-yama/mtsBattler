from models.monsterstate import MonsterState
import unittest
from unittest.mock import Mock, patch


class TestMonsterState(unittest.TestCase):
    def test_set_monster(self):
        monster = unittest.mock.MagicMock()
        monster.player = 1
        monster.team = 'teamA'
        monster.name = 'abc'
        monster.hp = 100

        m = MonsterState()
        m.set_monster(monster.player, monster)

        self.assertEqual(m.player, monster.player)
        self.assertEqual(m.team, monster.team)
        self.assertEqual(m.name, monster.name)
        self.assertEqual(m.hp, monster.hp)
        self.assertEqual(m.charge, 0)

    def test_set_state(self):
        monster_state = {
            'player': 1,
            'team': 'teamA',
            'name': 'abcx',
            'hp': 100,
            'charge': 5
        }
        expected = {
            'player': 1,
            'team': 'teamA',
            'name': 'abcx',
            'hp': 100,
            'charge': 5
        }
        m = MonsterState()
        m.set_states(monster_state)
        self.assertEqual(m.player, expected['player'])
        self.assertEqual(m.team, expected['team'])
        self.assertEqual(m.name, expected['name'])
        self.assertEqual(m.hp, expected['hp'])
        self.assertEqual(m.charge, expected['charge'])


if __name__ == '__main__':
    unittest.main()
