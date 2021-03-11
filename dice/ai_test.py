"""unittest ai."""
import unittest
from unittest.mock import MagicMock
import ai


class TestAiClass(unittest.TestCase):
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
        """Test set score function."""
        test = ai.AI("easy")
        test.scores = [1, 2, 3]
        test.set_score(4)
        res = 4 in test.scores
        self.assertTrue(res)

    def test_reset_score(self):
        """Test reset score function."""
        test = ai.AI("easy")
        test.scores = [1, 2, 3]
        test.reset_score()
        exp = []
        self.assertEqual(test.scores, exp)

    def test_get_turns(self):
        """Test get turn function."""
        test = ai.AI("easy")
        test.set_score(1)
        res = test.get_turns()
        exp = 1
        self.assertEqual(res, exp)

    def test_get_name(self):
        """Test get name function."""
        test = ai.AI('easy')
        test.set_name('abc')
        exp = test.get_name() == 'abc'
        self.assertTrue(exp)

    def test_set_name(self):
        """Test set name function."""
        test = ai.AI("easy")
        test.set_name("paul")
        exp = test.name == "paul"
        self.assertTrue(exp)

    def test_play_rolls_one(self):
        """Test object updated correctly when rolling 1."""
        obj = ai.AI('easy')
        obj.dice.roll = MagicMock(return_value=1)
        obj.play()
        res = obj.get_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_play_rolls_not_one(self):
        """Test object updated correctly when not rolling 1."""
        obj = ai.AI('easy')
        obj.dice.roll = MagicMock(return_value=6)
        obj.play()
        print(obj.scores)
        res = obj.get_score()
        exp = 12
        self.assertEqual(res, exp)

    def test_play_breaks_loop(self):
        """Check play method breaks loop when score >= 100."""
        obj = ai.AI('easy')
        obj.set_score(99)
        obj.dice.roll = MagicMock(return_value=6)
        obj.play()
        res = obj.get_score()
        exp = 105
        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
