"""AI module for computer game actions."""

import die
import dicehand


class AI:
    """AI class for game logic."""

    scores = []
    total_rolls = 0
    difficulty = 'easy'
    turn = None
    name = 'The computer'

    def __init__(self, difficulty):
        """Initialise object and set difficulty."""
        self.difficulty = difficulty
        self.turn = dicehand.Dicehand()

    def get_score(self):
        """Return the total score for this game."""
        return sum(self.scores)

    def set_score(self, value):
        """Add a score to the scores list."""
        self.scores.append(value)

    def reset_score(self):
        """Reset object score to empty list."""
        self.scores = []

    def get_turns(self):
        """Return the total amount of turns this game."""
        return len(self.scores)

    def get_name(self):
        """Return the name for AI."""
        return self.name

    def play(self):
        """AI logic to take a turn."""
        dice = die.Die()
        hold_total = (7 if self.difficulty == 'easy' else 20)
        while self.turn.get_total() < hold_total:
            number = dice.roll()
            print(f'Computer rolled a {number}')
            if number == 1:
                total = self.turn.get_total()
                print(f"Computer rolled a {number} and lost {total} points")
                self.turn.reset()
                break
            else:
                self.turn.increment(number)
                if self.get_score() + self.turn.get_total() >= 10:
                    break
        total = self.turn.get_total()
        self.set_score(total)
        self.turn.reset()
