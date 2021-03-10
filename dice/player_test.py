import unittest

import player


class PlayerTest(unittest.TestCase):
    """Test player class."""

    def test_init_default_object(self):
        """Instantiate object and check properties."""
        res = player.Player('Paul')
        exp = player.Player
        self.assertIsInstance(res, exp)

    def test_get_name(self):
        """Get players name and check it is correct."""
        test_player = player.Player('Paul')
        res = test_player.get_name()
        exp = 'Paul'
        self.assertEqual(res, exp)

    def test_set_name(self):
        """Update players name and check its value."""
        test_player = player.Player('Paul')
        test_player.set_name('Joselyn')

        res = test_player.get_name()
        exp = 'Joselyn'
        self.assertEqual(res, exp)

    def test_set_score(self):
        """Check the scores list is updated correctly."""
        test_player = player.Player('Paul')
        test_player.set_score(0)
        res = test_player.scores[-1]
        exp = 0
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
