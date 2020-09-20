import unittest
from models.monster import Monster, MonsterList
from unittest.mock import Mock, patch


class TestMonster(unittest.TestCase):
    def test_set_params(self):
        params = {
            'name': 'xyz',
            'team': 'teamA',
            'hp': 100,
            'image_path': '/tmp/test.png'
        }
        expected = {
            'name': 'xyz',
            'team': 'teamA',
            'hp': 100,
            'image_path': '/tmp/test.png'
        }
        monster = Monster()
        monster.set_params(params)

        self.assertEqual(monster.name, expected['name'])
        self.assertEqual(monster.team, expected['team'])
        self.assertEqual(monster.hp, expected['hp'])
        self.assertEqual(monster.image_path, expected['image_path'])

    def test_generate(self):
        team = 'teamB'
        name = 'abc'

        with patch('models.summon.Summon.generate_parameters_by_name') as mock_methed:
            monster = Monster()
            monster.generate(team, name)

            self.assertEqual(monster.team, team)
            self.assertEqual(monster.name, name)
            mock_methed.assert_called_with(name)


if __name__ == '__main__':
    unittest.main()
