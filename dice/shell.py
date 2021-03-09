"""Shell Module."""

import cmd
import game
import ai
import highscore
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
        if len(self.game.current_players) == 0:

            print(
                "\nYou need some players first.\n" +
                "Use command add_player to add a new player. " +
                "Maximum two players, Minimum one player\n" +
                "eg. add_player John\n"
                  )
        # Start the game if players were found.
        else:
            self.game.start()

    def do_add_player(self, name):
        """Add a player to the game. add_player <name>."""
        msg = self.game.add_player(name)
        print(msg)

    def do_remove_player(self, name):
        """Remove a player. remove_player <name>."""
        msg = self.game.remove_player(name)
        print(msg)

    def do_create_player(self, name):
        """Create a new player. create_player <name>."""
        self.game.create_player(name)

    def do_delete_player(self, name):
        """Delete a saved player. delete_player <name>."""
        self.game.delete_player(name)

    def do_roll(self, _):
        """Roll the dice."""
        if self.game.game_active:
            number, total = self.game.roll()
            if number == 1:
                print(f"You rolled a {number} and lost {total} points")
                print(self.game.display_scores())
            else:
                print(f"You rolled a {number}")
                print(f"Turn total -> {total}")
        else:
            print("You must start the game first with command start")

    def do_hold(self, _):
        """Save the turn points."""
        if self.game.game_active:
            self.game.hold()
            self.game.display_scores()
        else:
            print("You must start the game first with command start")

    def do_set_difficulty(self, arg):
        """Set the games difficulty. Options are easy or hard.

        set_difficulty hard
        set_difficulty easy
        """
        if arg in ['easy', 'hard']:
            self.game.set_difficulty(arg)
        else:
            print("Valid options are easy or hard")

    def do_exit(self, _):
        """Exit the game."""
        self.game.exit()
        print("Thanks for playing! See you next time")
        return True  # Returning true breaks the cmd loop

    def postcmd(self, stop, line):
        """Check the game state and perform actions needed."""
        command = line.split(' ')[0]

        if command in ['roll', 'hold'] and self.game.game_active:

            active_player = self.game.active_player

            has_winner, winner = self.game.check_for_winner()

            if has_winner:
                print(f"{winner.get_name()} won in {winner.get_turns()} turns")

                if isinstance(winner, player.Player):
                    winner.update_highscore(winner.get_turns())
                    file_name = 'highscores.pickle'
                    players = self.game.players
                    highscore.save_player_data(file_name, players)

                return True

            if isinstance(active_player, ai.AI):
                self.game.machine.play()
                self.game.toggle_active()
                self.game.display_scores()
                return False

        if self.game.game_active:
            self.prompt = self.set_prompt()

        if command == 'exit':
            return True

        return False

    def set_prompt(self):
        """Set the prompt to the players name."""
        return f"({self.game.active_player.name}) "
