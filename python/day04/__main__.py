"""Run the script."""
import collections
import math
import pathlib

from utils import inputs

from . import passport

INPUT_PATH = inputs.input_path(4, "passports")
assert INPUT_PATH.exists(), INPUT_PATH


if __name__ == "__main__":
    # inputs
    inputs = INPUT_PATH.read_text().strip()
    passports = passport.parse_input(inputs)

    num_valid = collections.Counter(
        passport.is_passport_valid(p) for p in passports
    )

    print(f"Total valid: {num_valid[True]}")
