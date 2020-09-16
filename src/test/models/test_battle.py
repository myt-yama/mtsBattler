import sys
import os
import unittest
from unittest.mock import Mock, patch

sys.path.append('../../')
sys.path.append('./')
from models.battle import Battle


class TestBattle(unittest.TestCase):
    @patch('models.battle.Battle.get_parameter')
    def test_get_battle_params(self, mock_get_parameter):
        mock_get_parameter.return_value = 'test_val'
        battle = Battle()
        expected = 100
        setattr(battle, 'test_val', expected)
        self.assertEqual(battle._get_battle_params( 0, 'test_val'), expected)
        self.assertEqual(mock_get_parameter.call_args.args,
                         (1, 'test_val'))

if __name__ == '__main__':
    unittest.main()
