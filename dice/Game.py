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
        """Set the starting values for player totals."""
        self.player1_total = 0
        self.player2_total = 0

    def add_player(self, new_player):
        """Add a player to the players array."""
        self.players.append(new_player)
