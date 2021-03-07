"""Main class for the game logic."""

import random


class Game:
    """Game class."""

    players = []
    player1_total = None
    player2_total = None
    goal = 100

    def __init__(self):
        """Init the object."""
        random.seed()

    def start(self):
        """Set the starting values for players scores."""
        self.player1_total = 0
        self.player2_total = 0

    def add_player(self, new_player):
        """Add a player to the players array."""
        self.players.append(new_player)

    def show_players(self):
        """Return a msg showing the players."""
        msg = "No players found!"

        if len(self.players) == 1:
            msg = f"Player 1: {self.players[0].get_name()}"
        else:
            msg = (f"Player 1: {self.players[0].get_name()} || " +
                   f"Player 2: {self.players[1].get_name()}")

        return msg

    def get_players(self):
        """Get players from players array."""
