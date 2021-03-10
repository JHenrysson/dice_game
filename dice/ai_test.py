"""unittest ai."""
import unittest
import ai
import dicehand
import die

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
        test.scores = [1,2,3]
        res = test.get_score()
        exp = 6
        self.assertEqual(res, exp)
        



if __name__ == '__main__':
    unittest.main()
