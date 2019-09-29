""" calling_frame.py """
import inspect


class CallingFrame(object):
    def __init__(self):
        self.__frame_info = inspect.stack()[1]

    @property
    def locals(self):
        return self.__frame_info.frame.f_locals
