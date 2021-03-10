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


if __name__ == '__main__':
    unittest.main()
