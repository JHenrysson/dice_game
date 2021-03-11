"""AI module for computer game actions."""

import die
import dicehand


class AI:
    """AI class for game logic."""

    scores = []

    def __init__(self, difficulty):
        """Initialise object and set difficulty."""
        self.difficulty = difficulty
        self.turn = dicehand.Dicehand()
        self.name = ('PIG Rookie' if difficulty == 'easy' else 'PIG Expert')
        self.dice = die.Die()
        self.scores = []

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

    def set_name(self, name):
        """Set the objects name."""
        self.name = name

    def play(self):
        """AI logic to take a turn."""
        hold_total = (7 if self.difficulty == 'easy' else 20)

        while self.turn.get_total() < hold_total:
            number = self.dice.roll()

            if number == 1:
                total = self.turn.get_total()
                print(f"{self.name} rolled a {number}. Lost {total} points\n")
                self.turn.reset()
                break

            print(f'{self.name} rolled a {number}\n')
            self.turn.increment(number)
            if self.get_score() + self.turn.get_total() >= 100:
                break  # Break the loop if winning score

        total = self.turn.get_total()
        self.set_score(total)
        print(f"{self.name} scored {total} points this turn\n")
        self.turn.reset()
