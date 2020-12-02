import collections


def is_row_valid_sleigh(row: str) -> bool:
    """Parse a row according to rules of day 2.

        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc

        min-max letter: password

    Check that password contains at least min and at most max instances of
    letter
    """
    # parse parts of string
    rules, sample = row.split(": ")
    nums, letter = rules.split(" ")
    min_, max_ = (int(x) for x in nums.split("-"))

    # check
    counter = collections.Counter(sample)
    return counter[letter] >= min_ and counter[letter] <= max_


def is_row_valid_toboggan(row: str) -> bool:
    """Parse a row according to rules of day 2.

        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc

        index0-index1 letter: password

    Check that password contains exactly one instance of letter at index0
    xor index1,
    """
    # parse parts of string
    rules, sample = row.split(": ")
    nums, letter = rules.split(" ")
    index0, index1 = (int(x) for x in nums.split("-"))

    # check
    return (sample[index0 - 1] == letter) != (sample[index1 - 1] == letter)
