"""Shell Module."""

import cmd
import game


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
        msg = self.game.add_player(name)
        print(msg)

    def do_remove_player(self, name):
        """Remove a player."""
        msg = self.game.remove_player(name)
        print(msg)

    def do_create_player(self, name):
        """Create a new player."""
        self.game.create_player(name)

    def do_delete_player(self, name):
        """Delete a saved player."""
        self.game.delete_player(name)

    def do_exit(self, _):
        """Exit the game."""
        self.game.exit()
        print("Thanks for playing! See you next time")
        return True  # Returning true breaks the cmd loop
