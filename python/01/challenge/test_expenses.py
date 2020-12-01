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
    expected_product = 514579
    expectd_sum = 2020

    # act
    actual_nums = expenses.find_inputs_which_sum_to(
        fixture_expenses, expectd_sum, 2
    )
    actual_product = actual_nums[0] * actual_nums[1]

    # assert
    assert actual_nums == {1721, 299}
    assert actual_product == expected_product
