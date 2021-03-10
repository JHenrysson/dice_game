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
        
    def test_set_score(self):
        test = ai.AI("easy")
        test.scores = [1,2,3]
        test.set_score(4)
        res = 4 in test.scores
        self.assertTrue(res)

    def test_reset_score(self):
        test = ai.AI("easy")
        test.scores = [1]
        test.reset_score
        res = not test.scores
        self.assertTrue(res)

    def test_get_name(self):
        """Test get name function."""
        test = ai.AI("easy")
        exp = test.get_name == 'PIG Rookie' or 'PIG Expert'
        self.assertTrue(exp)
        
if __name__ == '__main__':
    unittest.main()
