import inspect
import random

from time import sleep
from unittest import TestCase

import chronomancy


class Test(object):
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


class TestRecall(TestCase):

    def setUp(self):
        """ Setup the test class instance. """
        self.test = Test()

    def becomes_expected(self, current_value, expected_value, target_arg_pos: int = 0) -> bool:
        """
        A helper function to check if the current value becomes the expected value.

        Args:
            current_value (Any): The current value.
            expected_value (Any): The expected value.
            target_arg_pos (int): The target argument position.

        Returns:
            bool: True if the current value becomes the expected value, False otherwise.

        """
        calling_frame = inspect.stack()[1]
        sleep_time = 0.25
        timeout = 0

        found_expected = False

        while timeout < self.test.max_timeout:
            if current_value != expected_value:
                sleep(sleep_time)
                current_value = chronomancy.arcane_recall(calling_frame, target_argument_pos=target_arg_pos)
                print('Expected: {0}, Found: {1}'.format(expected_value, current_value))
                timeout += sleep_time
            else:
                found_expected = True
                break

        return found_expected

    def test_arcane_recall_works_with_class_instance_properties(self):
        assert self.becomes_expected(self.test.rand_property, 10)

    def test_arcane_recall_works_with_class_methods(self):
        assert self.becomes_expected(self.test.rand_method(), 10)

    def test_arcane_recall_works_defined_argument_position(self):
        assert self.becomes_expected(10, self.test.rand_method(), 1)
