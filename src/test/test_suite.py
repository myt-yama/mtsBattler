import unittest

from .models.test_battle import TestBattle
from .models.test_monsterstate import TestMonsterState
from .models.test_monster import TestMonster
from .models.test_summon import TestSummon


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestBattle.test_set_monsters)
    suite.addTest(TestBattle.test_set_states)
    suite.addTest(TestBattle.test_set_commands)

    suite.addTest(TestMonsterState.test_set_monster)
    suite.addTest(TestMonsterState.test_set_state)

    suite.addTest(TestMonster.test_set_params)
    suite.addTest(TestMonster.test_generate)

    suite.addTest(TestSummon.test_generate_parameters_by_name)
    suite.addTest(TestSummon.test_assign_image)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
