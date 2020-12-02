import pathlib

INPUT_DIRECTORY = pathlib.Path(__file__).parent / "../input/"


def input_path(day: int, name: str) -> pathlib.Path:
    return INPUT_DIRECTORY / f"day{day:02d}/{name}"
