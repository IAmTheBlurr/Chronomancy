""" Recalls the method or class property used as an input parameter by the calling frame"""
import warnings
import functools

from . import Chronomancy


def deprecated(func):
    """ This is a decorator which can be used to mark functions as deprecated. """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """ Wrapper function for deprecated functions """
        warnings.warn(
            f'Function {func.__name__} is deprecated and will be removed in a future version. '
            'Please use the Chronomancy class instead and instantiate it where you would have defined '
            'the calling_frame parameter originally. (Official Documentation coming soon... I hope...)',
            category=DeprecationWarning,
            stacklevel=2
        )
        return func(*args, **kwargs)
    return wrapper


@deprecated
def arcane_recall(calling_frame, target_argument_pos=0):
    """
    DEPRECATED: Use the Chronomancy class instead.

    Recalls the method or class property used as an input parameter by the calling frame.

    Args:
        calling_frame: The frame from which to recall the method.
        target_argument_pos: The position of the target argument.

    Returns:
        The result of recalling the specified method or class property.
    """
    # Create an instance of Chronomancy with a pre-captured frame
    chrono = Chronomancy.__new__(Chronomancy)  # Create instance without calling __init__
    chrono.anchor_frame = calling_frame  # Manually set the anchor_frame

    # Use the new implementation
    return chrono.arcane_recall(target_argument_pos)
