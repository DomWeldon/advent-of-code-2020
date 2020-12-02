"""Run the script."""
import math
import pathlib

from utils import inputs

from . import expenses

INPUT_PATH = inputs.input_path(1, "expenses")
assert INPUT_PATH.exists(), INPUT_PATH


if __name__ == "__main__":
    # get input
    inputs = [int(x) for x in INPUT_PATH.read_text().splitlines()]

    for n in [2, 3]:
        # find expenses
        answer = expenses.find_inputs_which_sum_to(inputs, target := 2020, n)

        # multiply together
        final_product = math.prod(answer)

        # tell the user
        answers = ", ".join(f"{a:,d}" for a in answer)
        print(
            (
                f"The {n} expenses which sum to {target:,d} are {answers}, "
                f"their product is {final_product:,d}"
            )
        )
