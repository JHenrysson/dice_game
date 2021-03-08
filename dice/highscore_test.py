"""Highscore class tests."""

import unittest
import highscore
import os
import pickle
import unittest.mock as mock


class TestHighscoreClass(unittest.TestCase):
    """Tests for the highscore class."""

    def test_file_created_when_non_existent(self):
        """Check file is created when not found."""
        no_file = os.path.exists('test.pickle')
        self.assertFalse(no_file)

        highscore.save_player_data('test.pickle', {'test': 1})
        file_exists = os.path.exists('test.pickle')
        self.assertTrue(file_exists)
        os.remove('test.pickle')

    def test_get_player_data(self):
        """Test data is retrieved correctly."""
        # Create test data
        test_data = pickle.dumps({'a': 1, 'b': 2, 'c': 3})
        # Create a mock open object
        test_open = mock.mock_open(read_data=test_data)

        # patch the open method with the mock and call it
        with mock.patch('builtins.open', test_open):
            obj = highscore.get_player_data('testpath')
        # Assert the values are equal
        self.assertEqual({'a': 1, 'b': 2, 'c': 3}, obj)

    def test_get_player_data_handles_exception(self):
        """Test exception raised when no file found."""
        with self.assertRaises(FileNotFoundError):
            highscore.get_player_data('invalid_path')