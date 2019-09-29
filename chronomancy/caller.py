""" caller.py """
import re


class Caller(object):
    def __init__(self, frame, target_argument=0, debug=False):
        self.__argument_pattern = re.compile('\\(.*\\)')
        self.__debug = debug
        self.__frame = frame
        self.__raw_command = self.__frame.code_context[0].strip('\n').strip(' ')
        self.__target_argument = target_argument

        self.__caller_arguments = []
        self.__method = None

        if not debug:
            self.build()

    def __call__(self):
        self.__method()

    @property
    def caller_arguments(self):
        if not self.__caller_arguments:
            self.__caller_arguments = self.__argument_pattern.search(self.__raw_command)[0].strip('\\(').strip('\\)').split(', ')

        return self.__caller_arguments

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = value

    def delete_target_argument_position(self):
        if 'target_arg_pos' in self.caller_arguments[-1]:
            del (self.caller_arguments[-1])

        return self.caller_arguments

    def delete_arguments_in_front_of_target(self):
        del (self.caller_arguments[:self.__target_argument])
        return self.caller_arguments

    def build(self):
        self.__caller_arguments = self.caller_arguments

        if self.__target_argument:
            self.delete_target_argument_position()
            self.delete_arguments_in_front_of_target()
            self.method = ', '.join(self.caller_arguments)
        else:
            self.method = ', '.join(self.caller_arguments[:-1])
