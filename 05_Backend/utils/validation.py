"""
Common input validation helpers for Saru POS.
"""


def is_string(value):
    return isinstance(value, str)


def is_non_empty_string(value):
    return isinstance(value, str) and bool(value.strip())


def is_number(value):
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
    )


def is_integer(value):
    return (
        isinstance(value, int)
        and not isinstance(value, bool)
    )