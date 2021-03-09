"""Highscore module to handle storing and retrieving highscore data."""

import pickle


def save_player_data(file_name, players):
    """Update the highscores."""
    try:
        with open(file_name, 'wb') as _file:
            pickle.dump(players, _file)
    except pickle.PicklingError:
        print("Error: Pickling error!")


def get_player_data(file_path):
    """Get the highscores data."""
    scores = {}

    try:
        with open(file_path, 'rb') as _file:
            scores = pickle.load(_file)
    except FileNotFoundError:
        print('File could not be found!')
        raise

    return scores
