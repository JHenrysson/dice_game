"""unittest AI class. """

import AI
import unittest

class TestAI(unittest.TestCase):
    """Test for the AI."""

    def test_init_default_object(self):
        """Initiate objects and check its properties. """
        res = AI.AI()
        exp = AI.AI
        self.assertIsInstance(res, exp)

    def test_get_AI_score(self):
        """Check get the AI score."""
        test_AI = AI.AI()
        res = test_AI.get_AI_score
        exp = 0
        self.assertEqual(res, exp)
    
    def test_set_AI_score(self):
        """check set AI score function."""
        res = AI.AI().set_AI_score(8)
        exp = AI.AI().get_AI_score + 8
        self.assertEqual(res, exp)
    
    def test_add_score_list(self):
        """check add score to the list function. """
        res = AI.AI().add_score_list(1)
        exp = AI.AI().get_last_score
        self.assertEqual(res,exp)
    
    def test_get_last_score(self):
        """check get last score function."""
        test_AI = AI.AI()
        exp = test_AI.get_last_score
        res = test_AI.add_score_list(1)
        self.assertEqual(res, exp)
    
    



