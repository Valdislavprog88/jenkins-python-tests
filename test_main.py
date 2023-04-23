import unittest
from parameterized import parameterized

from main import min_of_three_vars, make_capital_letters, division_by_twelve


class MinOfThreeVarsTestCase(unittest.TestCase):
    @parameterized.expand([
        ("first value min", (1, 2, 3), 1),
        ("second value min", (2, 1, 3), 1),
        ("third value min", (3, 2, 1), 1),
    ])
    def test_min(self, name, input, expected):
        self.assertEqual(min_of_three_vars(*input), expected)


class EchoFunctionTestCase(unittest.TestCase):
    @parameterized.expand([
        ("test", "TEST"),
        ("hello WORLD", "HELLO WORLD"),
        ("Lorem ipsum", "LOREM IPSUM"),
        ("tests are a cool thing!", "TESTS ARE A COOL THING!")
    ])
    def test_echo(self, input, expected):
        self.assertEqual(make_capital_letters(input), expected)


class DivisionFunctionTestCase(unittest.TestCase):
    @parameterized.expand([
        (12, True),
        (13, False),
        (15, False),
        (24, True),
    ])
    def test_division_by_twelve(self, input, expected):
        self.assertEqual(division_by_twelve(input), expected)
