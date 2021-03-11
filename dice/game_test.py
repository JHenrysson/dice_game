"""Unittests game."""

import unittest
import player
import game
import ai


class TestGameClass(unittest.TestCase):
    """Tests for the class."""

    def test_init_game_object(self):
        """Init the game object."""
        res = game.Game()
        exp = game.Game
        self.assertIsInstance(res, exp)

    def test_game_start_AI_is_added(self):
        """Check if ai object is added to players."""
        the_game = game.Game()
        the_game.create_player('Test')
        the_game.add_player('Test')
        the_game.start()

        res = the_game.current_players[1]
        self.assertIsInstance(res, ai.AI)

    def test_add_player_that_exists(self):
        """Check existing player added to current players correctly."""
        the_game = game.Game()
        the_game.create_player('Test')
        the_game.add_player('Test')
        res = the_game.current_players[0]
        self.assertIsInstance(res, player.Player)

    def test_add_player_adds_correct_player(self):
        """Check values on object to ensure it is correct object."""
        the_game = game.Game()
        the_game.create_player('Test')
        the_game.add_player('Test')
        res = the_game.current_players[0].get_name()
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
        """Check player is created properly with correct values."""
        the_game = game.Game()
        the_game.players = {}
        the_game.create_player('Test')
        obj = the_game.players['Test']
        self.assertIsInstance(obj, player.Player)
        res = obj.get_name()
        exp = 'Test'
        self.assertEqual(res, exp)

    def test_create_player_returns_correct_msg(self):
        """Check the correct message is returned."""
        the_game = game.Game()
        res = the_game.create_player('Test')
        exp = 'Test has been added to players'
        self.assertEqual(res, exp)

        res = the_game.create_player('Test')
        exp = 'That name is already taken! Try again.'
        self.assertEqual(res, exp)

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

    def test_update_player(self):
        """Check player is updated correctly."""
        the_game = game.Game()
        the_game.create_player('Test')
        the_game.update_player('Test', 'new name')
        the_player = the_game.players['new name']
        self.assertIsInstance(the_player, player.Player)

    def test_update_player_output_message(self):
        """Check update player returns correct output."""
        the_game = game.Game()
        the_game.create_player('Test')
        res = the_game.update_player('Test', 'new name')
        exp = 'Player Tests name has been updated to new name'
        self.assertEqual(res, exp)
        res = the_game.update_player('Not a player', 'new name')
        exp = 'Player Not a player does not exist.'
        self.assertEqual(res, exp)

    def test_toggle_active(self):
        """Check the active player is toggled correctly."""
        the_game = game.Game()
        the_game.create_player('player1')
        the_game.create_player('player2')
        the_game.add_player('player1')
        the_game.add_player('player2')
        the_game.start()
        res = the_game.active_player.get_name()
        exp = 'player1'
        self.assertEqual(res, exp)

        # Toggle the active player
        the_game.toggle_active()
        res = the_game.active_player.get_name()
        exp = 'player2'
        self.assertEqual(res, exp)

    def test_set_difficulty(self):
        """Check the difficulty is correctly changed."""
        the_game = game.Game()
        initial = the_game.machine.difficulty
        self.assertEqual(initial, 'easy')
        # Change the difficulty
        the_game.set_difficulty('hard')
        after = the_game.machine.difficulty
        self.assertEqual(after, 'hard')

    def test_roll(self):
        """Check roll returns correct values."""
        the_game = game.Game()
        the_game.create_player('1')
        the_game.add_player('1')
        the_game.start()
        first_roll, total_1_roll = the_game.roll()
        if first_roll == 1:
            self.assertEqual(total_1_roll, 0)
        else:
            self.assertEqual(first_roll, total_1_roll)
            second_roll, total_2_rolls = the_game.roll()
            if second_roll != 1:
                exp = first_roll + second_roll
                self.assertEqual(total_2_rolls, exp)

    def test_hold(self):
        """Check hold method updates values correctly."""
        the_game = game.Game()
        the_game.create_player('1')
        the_game.add_player('1')
        the_game.start()
        the_game.hold()
        players_score = the_game.current_players[0].scores[0]
        self.assertEqual(players_score, 0)
        res = the_game.active_player
        exp = the_game.current_players[1]
        self.assertEqual(res, exp)

    def test_check_for_winner(self):
        """Check the winning player is detected and returned."""
        the_game = game.Game()
        the_game.create_player('1')
        the_game.add_player('1')
        boolean, obj = the_game.check_for_winner()
        self.assertFalse(boolean)
        self.assertIsNone(obj)

        the_player = the_game.current_players[0]
        the_player.set_score(100)
        boolean, obj = the_game.check_for_winner()
        self.assertTrue(boolean)
        self.assertEqual(obj, the_player)

    def test_cheat(self):
        """Check for correct output when cheat."""
        self.assertEqual(game.Game().cheat(), 99)


if __name__ == '__main__':
    unittest.main()
