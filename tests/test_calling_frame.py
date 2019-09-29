""" test_calling_frame.py """
import pytest

from chronomancy import CallingFrame


@pytest.fixture
def calling_frame():
    local_test_int = 1
    local_test_string = 'Test String'
    print(local_test_int)
    print(local_test_string)
    return CallingFrame()


class TestCallingFrame(object):

    def test_calling_frame_has_expected_locals_mapped(self, calling_frame):
        assert 'local_test_int' in calling_frame.locals
        assert calling_frame.locals['local_test_int'] == 1
        assert 'local_test_string' in calling_frame.locals
        assert calling_frame.locals['local_test_string'] == 'Test String'
