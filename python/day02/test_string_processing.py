from . import string_processing


def test_is_row_valid_sleigh():
    # arrange
    fixtures = {
        "1-3 a: abcde": True,
        "1-3 b: cdefg": False,
        "2-9 c: ccccccccc": True,
    }

    # act
    valids = {k: string_processing.is_row_valid_sleigh(k) for k in fixtures}

    # assert
    assert all(valids[k] == fixtures[k] for k in fixtures)


def test_is_row_valid_toboggan():
    # arrange
    fixtures = {
        "1-3 a: abcde": True,
        "1-3 b: cdefg": False,
        "2-9 c: ccccccccc": False,
    }

    # act
    valids = {k: string_processing.is_row_valid_toboggan(k) for k in fixtures}

    # assert
    assert all(valids[k] == fixtures[k] for k in fixtures)
