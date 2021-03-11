"""unittest ai."""
import unittest
import ai


class TestaiClass(unittest.TestCase):
    """Test for ai class."""

    def test_init_ai_object(self):
        """Test object."""
        res = ai.AI("easy")
        exp = ai.AI
        self.assertIsInstance(res, exp)

    def test_get_score(self):
        """Test get score function."""
        test = ai.AI("easy")
        test.scores = [1, 2, 3]
        res = test.get_score()
        exp = 6
        self.assertEqual(res, exp)

    def test_set_score(self):
        """Check score is updated correctly."""
        test = ai.AI("easy")
        test.scores = [1, 2, 3]
        test.set_score(4)
        res = 4 in test.scores
        self.assertTrue(res)

    def test_reset_score(self):
        """Check score list is reset to empty list."""
        test = ai.AI("easy")
        test.scores = [1]
        test.reset_score()
        res = len(test.scores)
        exp = 0
        self.assertEqual(res, exp)

    def test_get_name(self):
        """Test get name function."""
        test = ai.AI("easy")
        res = test.get_name()
        exp = 'PIG Rookie'
        self.assertEqual(res, exp)

    def test_set_name(self):
        """Test set name function."""
        test = ai.AI("easy")
        test.set_name("paul")
        exp = test.name == "paul"
        self.assertTrue(exp)

    def test_get_turns(self):
        """Check the correct amount of turns are returned."""
        test = ai.AI('easy')
        test.scores = [1, 2, 3]
        res = test.get_turns()
        exp = 3
        self.assertEqual(res, exp)
        
   def test_lost_turn(self):
        test = ai.AI("easy")
        res = test.lost_turn(1)
        exp = test.turn.get_total() == 7 or 20
        self.assertEqual(res, exp)

    def test_max_score(self):
        test = ai.AI("easy")
        res = test.max_score(50, 60)
        exp = test.turn.get_total() == 7 or 20
        self.assertEqual(res, exp)

    def test_play(self):
        turn = dicehand.Dicehand()
        res = ai.AI("easy").play()
        res = turn.get_total()
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()
