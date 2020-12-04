"""Run the script."""
import math
import pathlib

from utils import inputs

from . import _types as task_types
from . import navigate

INPUT_PATH = inputs.input_path(3, "map")
assert INPUT_PATH.exists(), INPUT_PATH


if __name__ == "__main__":
    # inputs
    encounters = []
    for dx, dy in [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]:
        # get map
        text = INPUT_PATH.read_text().strip()
        array = navigate.parse_string_to_array(text.splitlines())
        len_down = len(array)
        gradient = dx / dy
        my_map = navigate.build_map_of_min_width(
            text, math.ceil(len_down * gradient)
        )

        encountered_trees = navigate.traverse_slope_count_val(
            my_map, dx, dy, task_types.Item.TREE
        )
        encounters.append(encountered_trees)

        forest = task_types.Item.TREE.value * encountered_trees
        print(
            f"Slope: {dx}, {dy}: encountered {encountered_trees} on "
            f"the way down: {forest}"
        )

    print(f"Total trees: {math.prod(encounters)}")
