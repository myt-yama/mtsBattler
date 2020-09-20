from models.battle import Battle
import unittest
from unittest.mock import Mock, patch


class TestBattle(unittest.TestCase):
    # @patch('models.battle.Battle.get_parameter')
    # def test_get_battle_params(self, mock_get_parameter):
    #     mock_get_parameter.return_value = 'test_val'
    #     battle = Battle()
    #     expected = 100
    #     setattr(battle, 'test_val', expected)
    #     self.assertEqual(battle._get_battle_params(0, 'test_val'), expected)
    #     self.assertEqual(mock_get_parameter.call_args.args,
    #                      (1, 'test_val'))

    def test_set_states(self):
        battle_state = {
            'turn': 3,
            'player_sum': 2
        }
        monster_state = [
            {
                'player': 1,
                'team': 'teamA',
                'name': 'abcx',
                'hp': 100,
                'charge': 5
            },
            {
                'player': 2,
                'team': 'teamB',
                'name': 'xyx',
                'hp': 50,
                'charge': 3
            }
        ]
        expected_battle = {
            'turn': 3,
            'player_sum': 2
        }
        expected_monster1 = {
            'player': 1,
            'team': 'teamA',
            'name': 'abcx',
            'hp': 100,
            'charge': 5
        }
        expected_monster2 = {
            'player': 2,
            'team': 'teamB',
            'name': 'xyx',
            'hp': 50,
            'charge': 3
        }
        battle = Battle()
        battle.set_states(battle_state, monster_state)
        self.assertEqual(battle.turn, expected_battle['turn'])
        self.assertEqual(battle.player_sum, expected_battle['player_sum'])

        m1 = battle.monster_states[1]
        self.assertEqual(m1.player, expected_monster1['player'])
        self.assertEqual(m1.team, expected_monster1['team'])
        self.assertEqual(m1.name, expected_monster1['name'])
        self.assertEqual(m1.hp, expected_monster1['hp'])
        self.assertEqual(m1.charge, expected_monster1['charge'])

        m2 = battle.monster_states[2]
        self.assertEqual(m2.player, expected_monster2['player'])
        self.assertEqual(m2.team, expected_monster2['team'])
        self.assertEqual(m2.name, expected_monster2['name'])
        self.assertEqual(m2.hp, expected_monster2['hp'])
        self.assertEqual(m2.charge, expected_monster2['charge'])

    def test_set_monsters(self):
        monster1 = unittest.mock.MagicMock()
        monster2 = unittest.mock.MagicMock()

        monster1.player = 1
        monster1.team = 'teamA'
        monster1.name = 'abc'
        monster1.hp = 100

        monster2.player = 2
        monster2.team = 'teamB'
        monster2.name = 'xyx'
        monster2.hp = 150

        monsters = [
            monster1,
            monster2
        ]
        battle = Battle()
        battle.set_monsters(monsters)

        self.assertEqual(battle.turn, 0)
        self.assertEqual(battle.player_sum, 2)

        m1 = battle.monster_states[1]
        self.assertEqual(m1.player, monster1.player)
        self.assertEqual(m1.team, monster1.team)
        self.assertEqual(m1.name, monster1.name)
        self.assertEqual(m1.hp, monster1.hp)
        self.assertEqual(m1.charge, 0)

        m2 = battle.monster_states[2]
        self.assertEqual(m2.player, monster2.player)
        self.assertEqual(m2.team, monster2.team)
        self.assertEqual(m2.name, monster2.name)
        self.assertEqual(m2.hp, monster2.hp)
        self.assertEqual(m2.charge, 0)

    def test_set_commands(self):
        commands = {
            1: 2,
            2: 0,
        }
        battle = Battle()
        battle.set_commands(commands)
        self.assertEqual(battle.commands, commands)

    def test_fight(self):
        pass


if __name__ == '__main__':
    unittest.main()
