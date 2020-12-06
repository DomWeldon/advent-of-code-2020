import functools
import operator as op
import string
import typing

from . import constants


def parse_declarations_anyone(
    inputs: str,
) -> typing.List[typing.Set[str]]:
    """Down and dirty list comp to parse input"""

    return [
        set(line) & set(string.ascii_lowercase)
        for line in inputs.split("\n\n")
    ]


def parse_declarations_everyone(
    inputs: str,
) -> typing.List[typing.Set[str]]:
    """Down and dirty list comp to parse input"""

    return [
        functools.reduce(op.and_, [set(line) for line in lines.splitlines()])
        for lines in inputs.split("\n\n")
    ]
