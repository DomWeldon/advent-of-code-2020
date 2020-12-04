from . import _types as task_types

ALL_KEYS = {"byr", "iyr", "eyr", "pid", "hgt", "hcl", "cid", "ecl"}
ALLOWED_MISSING_KEYS = {"cid"}
REQUIRED_KEYS = ALL_KEYS - ALLOWED_MISSING_KEYS

YEAR_RANGES = {
    "byr": (1920, 2002),
    "iyr": (2010, 2020),
    "eyr": (2020, 2030),
}
VALID_EYE_COLOURS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
