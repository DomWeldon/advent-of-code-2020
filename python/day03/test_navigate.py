import typing

import pytest

from . import _types as task_types
from . import constants, navigate

FIXTURE_MAP_TEXT = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
FIXTURE_MAP_EMOJI = """
⚫⚫🌲🌲⚫⚫⚫⚫⚫⚫⚫
🌲⚫⚫⚫🌲⚫⚫⚫🌲⚫⚫
⚫🌲⚫⚫⚫⚫🌲⚫⚫🌲⚫
⚫⚫🌲⚫🌲⚫⚫⚫🌲⚫🌲
⚫🌲⚫⚫⚫🌲🌲⚫⚫🌲⚫
⚫⚫🌲⚫🌲🌲⚫⚫⚫⚫⚫
⚫🌲⚫🌲⚫🌲⚫⚫⚫⚫🌲
⚫🌲⚫⚫⚫⚫⚫⚫⚫⚫🌲
🌲⚫🌲🌲⚫⚫⚫🌲⚫⚫⚫
🌲⚫⚫⚫🌲🌲⚫⚫⚫⚫🌲
⚫🌲⚫⚫🌲⚫⚫⚫🌲⚫🌲"""


@pytest.fixture(scope="session")
def fixture_map() -> typing.List[typing.List[bool]]:

    return [
        [constants.ITEM_MAP_LEGEND[c] for c in line]
        for line in FIXTURE_MAP_TEXT.splitlines()
        if line
    ]


def test_fixture_map(fixture_map):
    # arrange

    # act

    # assert
    assert (
        "\n".join("".join(c.value for c in line) for line in fixture_map)
        == FIXTURE_MAP_EMOJI.strip()
    )


def test_build_map_of_min_width(fixture_map):
    # arrange
    test_length = len(fixture_map[0])

    # act
    test_map = navigate.build_map_of_min_width(FIXTURE_MAP_TEXT, test_length)

    # assert
    assert len(test_map[0]) == test_length


def test_build_map_of_min_width_with_reps(fixture_map):
    # arrange
    original_length = len(fixture_map[0])
    test_length = original_length + 1

    # act
    test_map = navigate.build_map_of_min_width(FIXTURE_MAP_TEXT, test_length)

    # assert
    assert len(test_map[0]) == original_length * 2


def test_travese_slope_count_val():
    # arrange
    dx, dy = 3, 1
    fixture_array = navigate.build_map_of_min_width(FIXTURE_MAP_TEXT, 66)
    val = task_types.Item.TREE

    # act
    count = navigate.traverse_slope_count_val(fixture_array, dx, dy, val)

    # assert
    assert count == 7
