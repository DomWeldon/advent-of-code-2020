import string
import typing

from . import constants


def parse_input(
    s: str,
) -> typing.List[typing.Dict[str, str]]:
    """Down and dirty list comp to parse input"""
    return [
        {field.split(":")[0]: field.split(":")[1] for field in l}
        for l in [
            passport.strip().replace("\n", " ").split(" ")
            for passport in s.split("\n\n")
        ]
    ]


def is_passport_valid(passport: typing.Dict) -> bool:
    """Is the passport valid according to the rules?"""
    # check keys
    if not passport.keys() >= constants.REQUIRED_KEYS:
        return False

    # specific values
    byr = int(passport["byr"])
    if byr < 1920 or byr > 2002:
        return False

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    ranges = constants.YEAR_RANGES
    for k, (min_, max_) in ranges.items():
        if int(passport[k]) < min_ or int(passport[k]) > max_:
            return False

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    hgt = int(passport["hgt"][:-2])
    unit = passport["hgt"][-2:]
    ranges = {
        "cm": (150, 193),
        "in": (59, 76),
    }
    if unit not in ranges or hgt < ranges[unit][0] or hgt > ranges[unit][1]:
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hcl = passport["hcl"]
    hexes = set(string.hexdigits.lower())
    if not hcl.startswith("#") or set(hcl[1:]) > hexes:
        return False

    ecl = passport["ecl"]
    if ecl not in constants.VALID_EYE_COLOURS:
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pid = passport["pid"]
    if len(pid) != 9 or set(pid) > set(string.digits):
        return False

    return True
