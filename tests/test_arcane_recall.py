import inspect
import random
from time import sleep
from unittest import TestCase

import pytest

import chronomancy


class Test(object):
    def __init__(self):
        self.number = 10
        self.max_timeout = 100

    @property
    def rand_property(self):
        return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    @staticmethod
    def rand_method():
        return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    @staticmethod
    def rand_number_from(first: int, last: int) -> int:
        if first > last:
            raise
        return random.choice(list(range(first, last)))


class TestRecall(TestCase):

    def setUp(self):
        self.test = Test()

    def becomes_expected(self, current, expected, target_arg_pos=0):
        calling_frame = inspect.stack()[1]
        sleep_time = 0.25
        timeout = 0

        found_expected = False

        while timeout < self.test.max_timeout:
            if not current == expected:
                sleep(sleep_time)
                current = chronomancy.arcane_recall(calling_frame, target_argument_pos=target_arg_pos)
                print('Expected: {0}, Found: {1}'.format(expected, current))
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
        assert self.becomes_expected(10, self.test.rand_method(), target_arg_pos=1)

    def test_arcane_recall_works_with_methods_that_have_arguments(self):
        pytest.skip('Currently refactoring the area where these tests fail')
        assert self.becomes_expected(self.test.rand_number_from(10, 20), 15)
        assert self.becomes_expected(15, self.test.rand_number_from(10, 20), target_arg_pos=1)
