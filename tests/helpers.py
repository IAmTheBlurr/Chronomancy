""" A module to define helper classes and functions for testing. """
import random


class RandoHelper(object):
    """ A simple class to test the arcane_recall function. """
    def __init__(self):
        self.number = 10
        self.max_timeout = 100

    @property
    def rand_property(self) -> int:
        """
        Randomly returns a number between 1 and 10.

        Returns:
            int: A random number between 1 and 10.

        """
        return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    @staticmethod
    def rand_method() -> int:
        """
        Randomly returns a number between 1 and 10.

        Returns:
            int: A random number between 1 and 10.

        """
        return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])