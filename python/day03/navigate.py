import collections
import math
import typing

from . import _types as task_types
from . import constants


def parse_string_to_array(
    lines: typing.List[str],
) -> typing.List[typing.List[task_types.Item]]:
    """Parse my string to array"""
    return [[constants.ITEM_MAP_LEGEND[c] for c in line] for line in lines]


def build_map_of_min_width(s: str, min_width: int) -> typing.List[typing.List]:
    """Build a map repeated x times"""
    """Process the string map to an array.

    # => 🌲 => True
    . => no 🌲 => False
    """
    lines = [l.strip() for l in s.splitlines() if l]
    lengths = set(len(l) for l in lines)
    assert len(lengths) == 1

    original = parse_string_to_array(lines)

    rep = math.ceil(min_width / lengths.pop())

    return [line * rep for line in original]


def traverse_slope_count_val(
    array: typing.List[typing.List[task_types.Item]],
    dx: int,
    dy: int,
    val: task_types.Item,
) -> int:
    """Traverse the array and count instances of val encountered."""
    x, y = 0, 0
    encounters = collections.Counter()
    while y < len(array):
        # what do we encounter?
        encountered = array[y][x]
        encounters[encountered] += 1

        # move along the grid
        x += dx
        y += dy

    return encounters[val]
