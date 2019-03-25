import inspect
import random

from time import sleep
from unittest import TestCase

from totalrecall import recall


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


class TestRecall(TestCase):

    def setUp(self):
        self.test = Test()

    def becomes_expected(self, current, expected):
        calling_frame = inspect.stack()[1]
        sleep_time = 0.25
        timeout = 0

        found_expected = False

        while timeout < self.test.max_timeout:
            if not current == expected:
                sleep(sleep_time)
                current = recall.total_recall(calling_frame)
                print('Expected: {0}, Found: {1}'.format(expected, current))
                timeout += sleep_time
            else:
                found_expected = True
                break

        return found_expected

    def test_total_recall_works_with_class_instance_properties(self):
        assert self.becomes_expected(self.test.rand_property, 10)

    def test_total_recall_works_with_class_methods(self):
        assert self.becomes_expected(self.test.rand_method(), 10)
