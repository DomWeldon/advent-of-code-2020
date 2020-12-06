import string
import typing

from . import constants


def parse_boarding_pass(
    s: str,
) -> typing.Tuple[int, int]:
    """Down and dirty list comp to parse input"""
    row, col = s[:7], s[7:]
    return (
        int(row.replace("B", "1").replace("F", "0"), 2),
        int(col.replace("R", "1").replace("L", "0"), 2),
    )


def get_seat_id(seat: typing.Tuple[int, int]) -> int:
    return seat[0] * 8 + seat[1]


def find_missing_seat(seat_ids: typing.List[int]) -> int:
    """Find the missing seat in the middle of the number sequence"""
    seat_ids = set(seat_ids)
    for i in range(min(seat_ids), max(seat_ids)):
        if i not in seat_ids:
            return i

    raise ValueError()
