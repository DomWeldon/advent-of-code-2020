"""Run the script."""
import collections
import math
import pathlib

from utils import inputs

from . import seating

INPUT_PATH = inputs.input_path(5, "seating")
assert INPUT_PATH.exists(), INPUT_PATH


if __name__ == "__main__":
    # inputs
    inputs = INPUT_PATH.read_text().strip()
    seats = [seating.parse_boarding_pass(seat) for seat in inputs.splitlines()]

    seat_ids = [seating.get_seat_id(seat) for seat in seats]
    max_seat_id = max(seat_ids)

    print(f"Max seat ID: {max_seat_id}")

    missing_seat_id = seating.find_missing_seat(seat_ids)
    print(f"Missing seat ID: {missing_seat_id}")
