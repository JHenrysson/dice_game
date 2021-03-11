"""Die class module."""
import unittest

import die


class MyTestCase(unittest.TestCase):
    """Tests for die class."""

    def test_not_less_than_one(self):
        """Check roll value is greater than or equal to 1."""
        self.assertGreaterEqual(die.Die().roll(), 1)

    def test_not_greater_than_six(self):
        """Check roll value is less than or equal to six."""
        self.assertLessEqual(die.Die().roll(), 6)


if __name__ == '__main__':
    unittest.main()
