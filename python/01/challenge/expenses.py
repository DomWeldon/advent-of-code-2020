import itertools
import typing


def find_inputs_which_sum_to(inputs: typing.List[int], sum_to: int, n: int) -> typing.Set[int]:
    """Find the first n inputs which sum to sum_to"""
    for c in itertools.combinations(inputs, n):
        if sum(c) == sum_to:
            return set(c)
