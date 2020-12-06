# import pathlib
# import typing
#
# import pytest

from . import declarations


def test_parse_declarations_anyone():
    # arrange
    fixture_declarations = "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb\n"
    expected_declarations = [
        {"a", "c", "b"},
        {"a", "c", "b"},
        {"a", "c", "b"},
        {"a"},
        {"b"},
    ]

    # act
    actutal_declarations = declarations.parse_declarations_anyone(
        fixture_declarations
    )

    # assert
    assert actutal_declarations == expected_declarations


def test_parse_declarations_everyone():
    # arrange
    fixture_declarations = "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb\n"
    expected_declarations = [{"c", "b", "a"}, set(), {"a"}, {"a"}, {"b"}]

    # act
    actutal_declarations = declarations.parse_declarations_everyone(
        fixture_declarations
    )

    # assert
    assert actutal_declarations == expected_declarations


# def test_get_seat_ids():
#     # arrange
#     expected_seats = {
#         (44, 5): 357,
#         (14, 7): 119,
#         (102, 4): 820,
#     }
#
#     # act
#     actutal_seats = {k: seating.get_seat_id(k) for k in expected_seats}
#
#     # assert
#     assert actutal_seats == expected_seats
