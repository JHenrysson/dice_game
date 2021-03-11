"""Dicehand tests."""
import unittest

import dicehand


class MyTestCase(unittest.TestCase):
    """Tests for dicehand class."""

    def test_set_total(self):
        """Check set sets the total to 5."""
        hand = dicehand.Dicehand()
        hand.set_total(5)
        self.assertEqual(hand.get_total(), 5)

    def test_reset(self):
        """Check reset resets the total to 0."""
        hand = dicehand.Dicehand()
        hand.set_total(5)
        hand.reset()
        self.assertEqual(hand.get_total(), 0)

    def test_increment(self):
        """Check increment 1 increases the total by 1."""
        hand = dicehand.Dicehand()
        hand.increment(1)
        self.assertEqual(hand.get_total(), 1)

    def test_get_total(self):
        """Check get total is 0 at start."""
        self.assertEqual(dicehand.Dicehand().get_total(), 0)


if __name__ == '__main__':
    unittest.main()
