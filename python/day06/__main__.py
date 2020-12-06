"""Run the script."""
import collections
import math
import pathlib

from utils import inputs

from . import declarations

INPUT_PATH = inputs.input_path(6, "declarations")
assert INPUT_PATH.exists(), INPUT_PATH


if __name__ == "__main__":
    # inputs
    inputs = INPUT_PATH.read_text().strip()
    declarations_anyone = declarations.parse_declarations_anyone(inputs)
    declarations_everyone = declarations.parse_declarations_everyone(inputs)

    total_questions_anyone = sum(len(d) for d in declarations_anyone)
    total_questions_everyone = sum(len(d) for d in declarations_everyone)

    print(f"Total answered (anyone): {total_questions_anyone}")
    print(f"Total answered (everyone): {total_questions_everyone}")
