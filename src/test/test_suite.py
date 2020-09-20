import unittest

from .models.test_battle import TestBattle
from .models.test_monsterstate import TestMonsterState


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestBattle.test_set_monsters)
    suite.addTest(TestBattle.test_set_states)
    suite.addTest(TestBattle.test_set_commands)

    suite.addTest(TestMonsterState.test_set_monster)
    suite.addTest(TestMonsterState.test_set_state)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
