"""Player class."""


class Player:
    """Player class."""

    name = None

    def __init__(self, name):
        """Initialise the object."""
        self.name = name

    def get_name(self):
        """Return players name."""
        return self.name

    def set_name(self, name):
        """Update players name."""
        self.name = name
