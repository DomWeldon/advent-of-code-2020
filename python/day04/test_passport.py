import pathlib
import typing

import pytest

from . import constants, passport


@pytest.fixture(scope="function")
def fixture_input() -> str:

    return (pathlib.Path(__file__).parent / "fixtures/passports").read_text()


@pytest.fixture(scope="function")
def invalid_passports_input() -> typing.List[typing.Dict[str, str]]:

    return (
        pathlib.Path(__file__).parent / "fixtures/passports_invalid"
    ).read_text()


@pytest.fixture(scope="function")
def valid_passports_input() -> typing.List[typing.Dict[str, str]]:

    return (
        pathlib.Path(__file__).parent / "fixtures/passports_valid"
    ).read_text()


def test_passport_fixture(fixture_input):
    # arrange

    # act

    # assert
    assert fixture_input is not None


def test_parse_passports(fixture_input):
    # arrange

    # act
    passports = passport.parse_input(fixture_input)

    # assert
    assert len(passports) == 4
    assert len(passports[0]) == len(constants.ALL_KEYS)


def test_is_passport_valid(fixture_input):
    # arrange
    passports = passport.parse_input(fixture_input)

    # act
    valids = [passport.is_passport_valid(p) for p in passports]

    # assert
    assert valids == [True, False, True, False]


def test_is_passport_valid_on_invalid(invalid_passports_input):
    # arrange
    passports = passport.parse_input(invalid_passports_input)

    # act
    valids = {passport.is_passport_valid(p) for p in passports}

    # assert
    assert valids == {False}


def test_is_passport_valid_on_valid(valid_passports_input):
    # arrange
    passports = passport.parse_input(valid_passports_input)

    # act
    valids = {passport.is_passport_valid(p) for p in passports}

    # assert
    assert valids == {True}
