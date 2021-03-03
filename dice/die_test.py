import unittest

from dice.die import Die


class MyTestCase(unittest.TestCase):
    def test_not_less_than_one(self):
        self.assertGreaterEqual(Die().roll(), 1)


if __name__ == '__main__':
    unittest.main()
