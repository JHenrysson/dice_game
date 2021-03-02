import unittest

from dice.Player import Player


class PlayerTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual('testName', Player('testName').getName())


if __name__ == '__main__':
    unittest.main()
