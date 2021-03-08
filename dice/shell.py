"""Shell class."""

import cmd

from dice import game, player


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

    def do_exit(self, _):
        """Exit the game."""
        print("Thanks for playing! See you next time")
        return True  # Returning true breaks the cmd loop
