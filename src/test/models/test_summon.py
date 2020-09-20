from models.summon import Summon
import unittest
from unittest.mock import Mock, patch, MagicMock


class TestSummon(unittest.TestCase):
    def test_generate_parameters_by_name(self):
        name = 'abc'
        base_value = 124
        status_points = 50
        percentage = 0.5

        monster = MagicMock()
        summon = Summon(monster)
        summon._convert_string_to_int = MagicMock(return_value=base_value)
        summon._generate_status_points = MagicMock(return_value=status_points)
        summon._decide_percentage = MagicMock(return_value=percentage)
        summon._select_kanji = MagicMock()
        summon.assign_image = MagicMock()
        summon.assign_points_to_status = MagicMock()

        summon.generate_parameters_by_name(name)
        summon._convert_string_to_int.assert_called_with(name)
        summon._generate_status_points.assert_called_with(base_value)
        summon._decide_percentage.assert_called_with(base_value)
        summon._select_kanji.assert_called_with(name)
        summon.assign_image.assert_called_with(base_value)
        summon.assign_points_to_status.assert_called_with(
            status_points, percentage)

    def test_assign_image(self):
        monster = MagicMock()
        summon = Summon(monster)

        summon.assign_image(10)
        self.assertEqual(summon.monster.image_path,
                         '/static/img/blue_monster.png')
        summon.assign_image(55)
        self.assertEqual(summon.monster.image_path,
                         '/static/img/green_monster.png')
