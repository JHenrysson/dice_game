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

    def test_add_player_that_exists(self):
        """Check existing player added to current players correctly."""
        the_game = game.Game()
        the_game.create_player('Test')
        the_game.add_player('Test')
        res = the_game.current_players[0]
        exp = 'Test'
        self.assertEqual(res, exp)

    def test_add_player_that_doesnt_exist(self):
        """Check correct output when player non existant."""
        the_game = game.Game()
        the_game.players = {}
        res = the_game.add_player('invalid name')
        exp = "Player not found. Use command create_player first"
        self.assertEqual(res, exp)

    def test_add_player_when_list_full(self):
        """Check only two players can be added to the list."""
        the_game = game.Game()
        the_game.players = {'player3': 'Test'}
        the_game.current_players = ['player1', 'player2']
        res = the_game.add_player('player3')
        exp = "You already have 2 players. Use command remove_player first"
        self.assertEqual(res, exp)

    def test_create_player(self):
        """Check player is created properly."""
        the_game = game.Game()
        the_game.players = {}
        the_game.create_player('Test')
        self.assertIsInstance(the_game.players['Test'], player.Player)

    def test_remove_player(self):
        """Check a player can be removed from current players."""
        the_game = game.Game()
        the_game.current_players = ['player1', 'player2']
        the_game.remove_player('player1')
        res = 'player1' not in the_game.current_players
        self.assertTrue(res)

    def test_remove_player_output_success(self):
        """Check for correct output when player removed."""
        the_game = game.Game()
        the_game.current_players = ['player1', 'player2']
        res = the_game.remove_player('player1')
        exp = "player1 was removed from the game."
        self.assertEqual(res, exp)

    def test_remove_player_output_fail(self):
        """Check output when player not found in list."""
        the_game = game.Game()
        the_game.current_players = ['player1']
        res = the_game.remove_player('player2')
        exp = "player2 not found in player list."
        self.assertEqual(res, exp)

    def test_delete_player(self):
        """Check player is deleted from saved players."""
        the_game = game.Game()
        the_game.players = {'player1': 'test'}
        the_game.delete_player('player1')
        res = 'player1' not in the_game.players
        self.assertTrue(res)

    def test_delete_player_output_success(self):
        """Check for correct output when player deleted."""
        the_game = game.Game()
        the_game.players = {'player1': 'test'}
        res = the_game.delete_player('player1')
        exp = "player1 has been deleted."
        self.assertEqual(res, exp)

    def test_delete_player_output_fail(self):
        """Check for correct output when deleting non existent player."""
        the_game = game.Game()
        the_game.players = {}
        res = the_game.delete_player('player1')
        exp = "Player not found."
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
