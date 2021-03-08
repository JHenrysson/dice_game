"""Module for die class."""
import random


class Die:
    """Die class for game dice actions."""

    def __init__(self):
        """Initialise the dice object."""
        random.seed()

    # pylint: disable=no-self-use
    def roll(self) -> int:
        """Roll the dice to generate a number between 1 and 6."""
        return random.randint(1, 6)
