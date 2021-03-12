"""Main class for the game logic."""

import os
import player
import highscore
import die
import dicehand
import ai


# pylint: disable = too-many-instance-attributes
class Game:
    """Game class."""

    active_index = 0  # player 1 = 0 || player 2 = 1
    active_player = None
    game_active = False
    save_file = 'highscores.pickle'
    cheated = False

    def __init__(self):
        """Init the object."""
        self.machine = ai.AI('easy')
        self.turn = dicehand.Dicehand()
        self.dice = die.Die()
        self.current_players = []
        if os.path.exists(self.save_file):
            self.players = highscore.get_player_data(self.save_file)
        else:
            self.players = {}

    def start(self):
        """Set the starting values for players scores."""
        if len(self.current_players) == 1:  # Add AI object for 1 player game
            self.current_players.append(self.machine)
        self.game_active = True
        self.active_player = self.current_players[0]  # Set player 1 active
        self.turn.reset()  # Reset the turn score total
        for obj in self.current_players:
            obj.reset_score()  # Reset the scores for players if game restarts

    def add_player(self, name):
        """Add a player to the players array."""
        if len(self.current_players) == 2:
            msg = "You already have 2 players. Use command remove_player first"
        elif name in self.players:
            the_player = self.players[name]
            self.current_players.append(the_player)
            msg = f"{name} has been added to the game"
        else:
            msg = 'Player not found. Use command create_player first'

        return msg

    def create_player(self, name):
        """Create a new player and add them to players dictionary."""
        msg = f"{name} has been added to players"

        if name not in self.players:
            new_player = player.Player(name)
            self.players[name] = new_player
        else:
            msg = "That name is already taken! Try again."

        return msg

    def remove_player(self, name):
        """Remove a player from the game."""
        msg = f"{name} not found in player list."

        for obj in self.current_players:
            if obj.name == name:
                self.current_players.remove(obj)
                msg = f"{name} was removed from the game."

        return msg

    def delete_player(self, name):
        """Delete a player from saved players."""
        msg = f"{name} has been deleted."

        if name in self.players:
            self.players.pop(name)
        else:
            msg = 'Player not found.'

        return msg

    def update_player(self, name, new_name):
        """Update a players name."""
        msg = f"Player {name}s name has been updated to {new_name}"

        if name in self.players:
            self.players[new_name] = self.players.pop(name)
            self.players[new_name].set_name(new_name)

        else:
            msg = f"Player {name} does not exist."

        return msg

    def toggle_active(self):
        """Toggle active player."""
        self.active_index = int(not self.active_index)
        self.active_player = self.current_players[self.active_index]
        print(self.display_scores())

    def display_scores(self):
        """Display current scores."""
        player1 = self.current_players[0]
        player2 = self.current_players[1]

        msg = (f"{'Player':13} | {'Score':^5}\n" +
               f"{'-' * 21}\n" +
               f"{player1.get_name():13} | {player1.get_score():^5}\n" +
               f"{player2.get_name():13} | {player2.get_score():^5}\n")

        return msg

    def set_difficulty(self, value):
        """Set the games difficulty."""
        self.machine.difficulty = value  # Change the game difficulty setting
        new_name = ('PIG Rookie' if value == 'easy' else 'PIG Expert')
        self.machine.set_name(new_name)

    def roll(self):
        """Roll the dice and update players total."""
        the_player = self.active_player
        number = self.dice.roll()  # roll the dice
        total = self.turn.get_total()  # Get turn total before new score added

        if number == 1:
            self.active_player.set_score(0)  # Add 0 to players score
            print(f"You rolled a {number} and lost {total} points\n")
            self.turn.reset()  # reset turn total
            self.toggle_active()  # change active player

        else:
            self.turn.increment(number)  # Add to turn total
            total = self.turn.get_total()  # Get current total
            if the_player.get_score() + total >= 100:  # Check if player won
                the_player.set_score(total)  # Update players score
            print(f"You rolled -> {number}\n")
            print(f"Turn total -> {total}\n")

        return number, total  # Return value used in shell class to print msg

    def hold(self):
        """Add the points for the turn to players score."""
        total = self.turn.get_total()  # Get score for this turn
        the_player = self.active_player  # Select current player
        the_player.set_score(total)  # Add total to players score
        self.turn.reset()  # Reset the turn total to 0
        print(f"{the_player.get_name()} scored {total} point this turn\n")
        self.toggle_active()  # Change active player

    def check_for_winner(self):
        """Check for a winning score."""
        is_winner = False
        winner = None
        for obj in self.current_players:  # loop through players
            if obj.get_score() >= 100:  # Check if player has won
                is_winner = True
                winner = obj

        return is_winner, winner

    def cheat(self):
        """Cheat and update players total."""
        self.turn.set_total(99)  # Add to turn total
        total = self.turn.get_total()  # Get current total
        print(f"Turn total -> {total}\n")
        return total  # Return value used in shell class to print msg

    def get_players(self):
        """Get all players."""
        return self.players

    def restart(self):
        """Quit the current game and retart it."""
        self.turn.reset()
        for obj in self.current_players:
            obj.reset_score()
        print("Your current game has been restarted. ")
