"""Shell Module."""

import cmd
import game
import ai
import highscore
import player


class Shell(cmd.Cmd):
    """Shell class to run the game in command line."""

    intro = "Welcome to the game of PIG. Type help or ? to list commands."
    prompt = "(Lobby) "

    def __init__(self):
        """Initialise the object."""
        super().__init__()
        self.game = game.Game()

    def do_start(self, _):
        """Starts the game."""
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

    def do_restart(self, _):
        """Return the the lobby. With current players still active.

        Use command start to start the game again.
        """
        msg = self.game.restart()
        print(msg)

    def do_add_player(self, name):
        """Add a player to the game. add_player <name>."""
        msg = self.game.add_player(name)
        print(msg)

    def do_remove_player(self, name):
        """Remove a player from the game. remove_player <name>."""
        msg = self.game.remove_player(name)
        print(msg)

    def do_create_player(self, name):
        """Create a new player. create_player <name>."""
        self.game.create_player(name)

    def do_delete_player(self, name):
        """Delete a saved player. delete_player <name>."""
        self.game.delete_player(name)

    def do_change_name(self, arg):
        """Update an existing players name.

        change_name <old name> <new name>
        Eg. change_name John David
        """
        args = arg.split(' ')
        player_name = args[0]
        new_name = args[1]
        msg = self.game.update_player(player_name, new_name)
        print(msg)

    def do_roll(self, _):
        """Roll the dice."""
        if self.game.game_active:
            self.game.roll()
        else:
            print("You must start the game first with command start")

    def do_hold(self, _):
        """End your turn and save your score."""
        if self.game.game_active:
            self.game.hold()
            self.game.display_scores()
        else:
            print("You must start the game first with command start")

    def do_difficulty(self, arg):
        """Set the games difficulty. Options are easy or hard.

        difficulty hard
        difficulty easy
        """
        if arg in ['easy', 'hard']:
            self.game.set_difficulty(arg)
        else:
            print("Valid options are easy or hard")

    # pylint: disable=no-self-use
    def do_show_rule(self, _):
        """Display the game rules."""
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

    def do_cheat(self, _):
        """Cheat."""
        if self.game.game_active:
            self.game.cheat()
        else:
            print("You must start the game first with command start")

    def sort_highscore(self, e):
        """Sort by highest score."""
        return e.get_score()

    def do_highscore(self, _):
        """Show players highscores."""
        players = list(self.game.get_players().values())
        players.sort(key=self.sort_highscore, reverse=True)

        for highscore_player in players:
            print(highscore_player.get_name() + ': ' +
                  str(highscore_player.get_score()))

    def do_exit(self, _):
        """Exit the game."""
        print("Thanks for playing! See you next time")
        return True  # Returning true breaks the cmd loop

    def postcmd(self, stop, line):
        """Check the game state and perform actions needed."""
        command = line.split(' ')[0]

        if command in ['roll', 'hold'] and self.game.game_active:

            active_player = self.game.active_player

            if isinstance(active_player, ai.AI):
                self.game.machine.play()
                has_winner, winner = self.game.check_for_winner()
                self.game.toggle_active()

            has_winner, winner = self.game.check_for_winner()

            if has_winner:
                print(f"{winner.get_name()} won in {winner.get_turns()} turns")

                if isinstance(winner, player.Player):
                    winner.update_highscore(winner.get_turns())
                    file_name = self.game.save_file
                    players = self.game.players
                    highscore.save_player_data(file_name, players)

                return True

        if self.game.game_active:
            self.prompt = self.set_prompt()

        if command == 'restart':
            self.prompt = '(Lobby) '

        if command == 'exit':
            return True

        return False

    def emptyline(self):
        """Disable automatic calling of previous command on emptyline."""
        print('\nYou didnt enter a valid command!\n')
        return False

    def set_prompt(self):
        """Set the prompt to the players name."""
        return f"({self.game.active_player.name}) "
