# Source Generated with Decompyle++
# File: _itertools.pyc (Python 3.12)


def only(iterable, default, too_long = (None, None)):
    """If *iterable* has only one item, return it.
    If it has zero items, return *default*.
    If it has more than one item, raise the exception given by *too_long*,
    which is ``ValueError`` by default.
    >>> only([], default='missing')
    'missing'
    >>> only([1])
    1
    >>> only([1, 2])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    ValueError: Expected exactly one item in iterable, but got 1, 2,
     and perhaps more.'
    >>> only([1, 2], too_long=TypeError)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    TypeError
    Note that :func:`only` attempts to advance *iterable* twice to ensure there
    is only one item.  See :func:`spy` or :func:`peekable` to check
    iterable contents less destructively.
    """
    it = iter(iterable)
    first_value = next(it, default)
    
    try:
        second_value = next(it)
        msg = 'Expected exactly one item in iterable, but got {!r}, {!r}, and perhaps more.'.format(first_value, second_value)
        if not too_long:
            too_long
        raise ValueError(msg)
    except StopIteration:
        return first_value


