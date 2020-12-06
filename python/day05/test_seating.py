# import pathlib
# import typing
#
# import pytest

from . import seating


def test_parse_boarding_pass():
    # arrange
    expected_seats = {
        "BFFFBBFRRR": (70, 7),
        "FFFBBBFRRR": (14, 7),
        "BBFFBBFRLL": (102, 4),
    }

    # act
    actutal_seats = {k: seating.parse_boarding_pass(k) for k in expected_seats}

    # assert
    assert actutal_seats == expected_seats


def test_get_seat_ids():
    # arrange
    expected_seats = {
        (44, 5): 357,
        (14, 7): 119,
        (102, 4): 820,
    }

    # act
    actutal_seats = {k: seating.get_seat_id(k) for k in expected_seats}

    # assert
    assert actutal_seats == expected_seats
