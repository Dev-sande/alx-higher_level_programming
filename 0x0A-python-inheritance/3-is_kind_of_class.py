#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ Function that checks if obj is an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class type to compare against.

    Returns:
        True if obj is an instance of a_class.
        False otherwise.
    """
    return isinstance(obj, a_class)

