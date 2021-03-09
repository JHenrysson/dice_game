"""Main class for the game logic."""

import random

from dice.turn import Turn


class Game:
    """Game class."""

    players = []
    goal = 100

    def __init__(self):
        """Init the object."""
        random.seed()

    def start(self):
        """Set the starting values for players scores."""
        current_player = 1
        winner = False

        player = None

        while not winner:
            if current_player == 1:
                current_player = 0
            else:
                current_player = 1

            player = self.players[current_player]

            print(player[0].get_name() + '\'s turn')
            player[1] = Turn(player[1], self.goal).start()

            if player[1] >= self.goal:
                winner = True

        print('The winner is: ' + player[0].get_name())


    def add_player(self, new_player):
        """Add a player to the players array."""
        self.players.append([new_player, 0])

    def show_players(self):
        """Return a msg showing the players."""
        msg = "No players found!"

        if len(self.players) == 1:
            msg = f"Player 1: {self.players[0][0].get_name()}"
        else:
            msg = (f"Player 1: {self.players[0][0].get_name()} || " +
                   f"Player 2: {self.players[1][0].get_name()}")

        return msg

    def get_players(self):
        """Get players from players array."""
