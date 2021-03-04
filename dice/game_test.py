"""Unittests game."""

import unittest
import player
import game


class TestGameClass(unittest.TestCase):
    """Tests for the class."""

    def test_init_game_object(self):
        """Init the game object."""
        res = game.Game()
        exp = game.Game
        self.assertIsInstance(res, exp)

    def test_start_game(self):
        """Check values are initialised for players score."""
        the_game = game.Game()
        the_game.start()

        res = the_game.player1_total
        res2 = the_game.player2_total
        exp = 0
        self.assertEqual(res, exp)
        self.assertEqual(res2, exp)

    def test_add_player(self):
        """Check player added to players array correctly."""
        the_game = game.Game()
        new_player = player.Player('Paul')
        the_game.add_player(new_player)

        res = the_game.players[0]
        exp = new_player
        self.assertEqual(res, exp)

    def test_show_players(self):
        """Test whether player names are shown correctly."""
        the_game = game.Game()
        the_game.players = []

        player1 = player.Player('Paul')
        the_game.add_player(player1)

        res = the_game.show_players()
        exp = "Player 1: Paul"
        self.assertEqual(res, exp)

        player2 = player.Player('Xuan')
        the_game.add_player(player2)

        res = the_game.show_players()
        exp = "Player 1: Paul || Player 2: Xuan"
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()