"""Run the script."""
import collections
import pathlib

from utils import inputs

from . import string_processing

INPUT_PATH = inputs.input_path(2, "passwords")
assert INPUT_PATH.exists(), INPUT_PATH


if __name__ == "__main__":
    # get input
    rows = [x.strip() for x in INPUT_PATH.read_text().splitlines()]

    sleigh_count = collections.Counter(
        string_processing.is_row_valid_sleigh(row) for row in rows
    )
    toboggan_count = collections.Counter(
        string_processing.is_row_valid_toboggan(row) for row in rows
    )

    print(
        "🛷 Sleigh Policy",
        f"Number of valid rows: {sleigh_count[True]}",
        f"Number of invalid rows: {sleigh_count[False]}",
        "🧝 Toboggan Policy",
        f"Number of valid rows: {toboggan_count[True]}",
        f"Number of invalid rows: {toboggan_count[False]}",
        sep="\n",
    )
