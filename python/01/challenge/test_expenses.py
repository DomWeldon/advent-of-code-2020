import math

from . import expenses


def test_find_inputs_which_sum_to():
    # arrange
    fixture_expenses = [
        1_721,
        979,
        366,
        299,
        675,
        1_456,
    ]
    expected_product = 514_579
    expected_sum = 2_020

    # act
    actual_nums = expenses.find_inputs_which_sum_to(
        fixture_expenses, expected_sum, 2
    )
    actual_product = math.prod(actual_nums)

    # assert
    assert actual_nums == {1_721, 299}
    assert actual_product == expected_product
