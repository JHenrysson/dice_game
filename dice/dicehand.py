"""Dice Hand module."""


class Dicehand():
    """Class to keep track of each turn."""

    total = None

    def __init__(self):
        """Init the object."""
        self.total = 0

    def get_total(self):
        """Return the current total for the turn."""
        return self.total

    def increment(self, value):
        """Add the passed in value to the total."""
        self.total += value

    def set_total(self, value):
        """Set the passed in value as the total."""
        self.total = value

    def reset(self):
        """Reset the total to 0."""
        self.total = 0
