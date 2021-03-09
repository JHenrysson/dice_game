"""Shell class."""

import cmd
import game
import player


class Shell(cmd.Cmd):
    """Shell class to run the game in command line."""

    intro = "Welcome to the game of PIG. Type help or ? to list commands."
    prompt = "(PIG) "

    def __init__(self):
        """Initialise the object."""
        super().__init__()
        self.game = game.Game()

    def do_start(self, _):
        """Start the game and initialise values."""
        # Prompt user to add players if none present.
        if len(self.game.players) == 0:

            print(
                "\nYou need some players first.\n" +
                "Use command add_player to add a new player. " +
                "Maximum two players.\n" +
                "eg. add_player John\n"
                  )
        # Start the game if players were found.
        else:
            self.game.start()

    def do_add_player(self, name):
        """Add a player to the game."""
        if len(self.game.players) < 2:
            self.game.add_player(player.Player(name))
        else:
            print("You already have the maximum number of players!")

    def do_show_players(self, _):
        """Show the current players names."""
        msg = self.game.show_players()
        print(msg)
    
        def do_show_rule(self, _):
        """The rule of the game."""
        first_line = "Each turn, a player repeatedly rolls a die until either "
        second_line = "a 1 is rolled or the player decides to 'hold':"
        third_line = "If the player rolls a 1, they score nothing"
        fourth_line = " and the next player takes turn"
        fifth_line = "If the player rolls any other number, it is added "
        sixth_line = "to their turn total and the player's turn continues"
        seventh_line = "If a player chooses to 'hold', their turn total is "
        eight_line = "added to their score, and the next player takes."
        print(first_line + second_line)
        print(third_line + fourth_line)
        print(fifth_line + sixth_line)
        print(seventh_line + eight_line)

    def do_exit(self, _):
        """Exit the game."""
        print("Thanks for playing! See you next time")
        return True  # Returning true breaks the cmd loop
