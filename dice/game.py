# Change game winning total from 10 to 100

"""Main class for the game logic."""

import os
import player
import highscore
import die
import dicehand
import ai


class Game:
    """Game class."""

    players = {}
    current_players = []
    active_index = 1  # player 1 = 0 || player 2 = 1
    active_player = None
    game_active = False
    save_file = 'highscores.pickle'

    def __init__(self):
        """Init the object."""
        self.machine = ai.AI('easy')
        self.turn = dicehand.Dicehand()
        self.dice = die.Die()
        if os.path.exists(self.save_file):
            self.players = highscore.get_player_data(self.save_file)

    def start(self):
        """Set the starting values for players scores."""
        if len(self.current_players) == 1:
            self.current_players.append(self.machine)
        self.game_active = True
        self.toggle_active()
        self.turn.reset()
        for obj in self.current_players:
            obj.reset_score()

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
        msg = f"{name} was removed from the game."

        if name in self.current_players:
            self.current_players.remove(name)
        else:
            msg = f"{name} not found in player list."

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
        msg = f"Name has been updated to {new_name}"

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

    def display_scores(self):
        """Display current scores."""
        player1 = self.current_players[0]
        player2 = self.current_players[1]

        msg = (f"{player1.get_name():15} -> {player1.get_score()}\n" +
               f"{player2.get_name():15} -> {player2.get_score()}\n")

        return msg

    def set_difficulty(self, value):
        """Set the games difficulty."""
        self.machine.difficulty = value

    def roll(self):
        """Roll the dice and update players total."""
        the_player = self.active_player
        number = self.dice.roll()  # roll the dice
        total = self.turn.get_total()  # Get turn total before roll
        if number == 1:
            self.active_player.set_score(0)  # Add 0 to players score
            self.turn.reset()  # reset turn total
            self.toggle_active()  # change active player
        else:
            self.turn.increment(number)  # Add to turn total
            total = self.turn.get_total()  # Get current total
            if the_player.get_score() + total > 10:  # Check if player won
                the_player.set_score(total)  # Update players score
        return number, total  # Return value used in shell class to print msg

    def hold(self):
        """Add the points for the turn to players score."""
        turn_score = self.turn.get_total()  # Get score for this turn
        the_player = self.active_player  # Select current player
        the_player.set_score(turn_score)  # Add total to players score
        self.turn.reset()  # Reset the turn total to 0
        self.toggle_active()  # Change active player

    def check_for_winner(self):
        """Check for a winning score."""
        for obj in self.current_players:  # loop through players
            if obj.get_score() >= 10:  # Check if player has reach goal
                return True, obj
            else:
                return False, obj

    def exit(self):
        """Exit the game."""
        highscore.save_player_data(self.save_file, self.players)
