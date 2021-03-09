"""Turn class."""
from dice.die import Die


class Turn:
    """Turn class."""

    die = Die()
    name = None
    goal = None

    def __init__(self, score: int, goal: int):
        """Initialise the object."""
        self.score = score
        self.goal = goal

    def start(self) -> int:
        passed = False

        while not passed:
            choice = input('Roll or pass: ')
            if choice.lower() == "roll":
                roll = self.die.roll()
                print('You rolled: ' + str(roll))
                if roll == 1:
                    self.score = 0
                    passed = True
                else:
                    self.score += roll
                    if self.score >= self.goal:
                        passed = True

                print('Your total score is now ' + str(self.score))
            else:
                passed = True

        return self.score
