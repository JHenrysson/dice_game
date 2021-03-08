"""Player class."""


class Player:
    """Player class."""

    name = None
    highscore = None
    game_score = 0

    def __init__(self, name):
        """Initialise the object."""
        self.name = name

    def get_name(self):
        """Return players name."""
        return self.name

    def set_name(self, name):
        """Update players name."""
        self.name = name

    def get_game_score(self):
        """Return players score for current game."""
        return self.game_score

    def set_game_score(self, score):
        """Update players score for current game."""
        self.game_score += score
