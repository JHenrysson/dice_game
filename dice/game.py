"""Main class for the game logic."""

import os
import random
import player
import highscore


class Game:
    """Game class."""

    save_file = 'highscores.pickle'
    players = {}
    current_players = []
    player1_total = None
    player2_total = None
    goal = 100

    def __init__(self):
        """Init the object."""
        random.seed()
        if os.path.exists(self.save_file):
            self.players = highscore.get_player_data(self.save_file)

    def start(self):
        """Set the starting values for players scores."""
        self.player1_total = 0
        self.player2_total = 0

    def add_player(self, name):
        """Add a player to the players array."""
        if len(self.current_players) == 2:
            msg = "You already have 2 players. Use command remove_player first"
        elif name in self.players:
            self.current_players.append(name)
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

    def exit(self):
        """Exit the game."""
        highscore.save_player_data(self.save_file, self.players)

    def get_players(self):
        """Get players from players array."""
