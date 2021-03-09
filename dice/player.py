"""Player class."""


class Player:
    """Player class."""

    name = None
    highscore = None  # Winning the game in least amount of rolls
    scores = []

    def __init__(self, name):
        """Initialise the object."""
        self.name = name

    def get_name(self):
        """Return players name."""
        return self.name

    def set_name(self, name):
        """Update players name."""
        self.name = name

    def get_score(self):
        """Return players score for current game."""
        return sum(self.scores)

    def get_turns(self):
        """Return total turns player has taken."""
        return len(self.scores)

    def set_score(self, score):
        """Update players score for current game."""
        self.scores.append(score)

    def reset_score(self):
        """Reset object score to empty list."""
        self.scores = []

    def update_highscore(self, score):
        """Check if new highscore and update if it is."""
        if self.highscore is None:
            self.highscore = score
        elif self.highscore > score:
            self.highscore = score
