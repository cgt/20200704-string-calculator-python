import pytest

def test_empty_string_returns_zero():
    assert add("") == 0

def test_add_0_returns_0():
    assert add("0") == 0

def test_add_4_returns_4():
    assert add("4") == 4

def test_add_1_and_2_returns_3():
    assert add("1,2") == 3

def test_add_3_and_5_returns_8():
    assert add("3,5") == 8

def test_add_1_and_2_and_3_returns_6():
    assert add("1,2,3") == 6

def test_add_1_and_2_and_3_and_4_returns_10():
    assert add("1,2,3,4") == 10

def test_add_1_newline_2_comma_3_returns_6():
    assert add("1\n2,3") == 6

def test_add_with_custom_separator():
    assert add("//;\n1;2") == 3


def test_add_rejects_negative_numbers():
    with pytest.raises(Exception):
        add("-2")
    with pytest.raises(Exception):
        add("6,-7")

def add(separated_numbers):
    if separated_numbers == "":
        return 0
    if separated_numbers.startswith("//"):
        separated_numbers = normalize_custom_separator(separated_numbers)
    separated_numbers = normalize_separator(separated_numbers, ",")

    if "\n" in separated_numbers:
        return add_separated_numbers(separated_numbers, "\n")

    n = int(separated_numbers)
    if n < 0:
        raise Exception
    return n


def normalize_custom_separator(separated_numbers):
    parts = separated_numbers.split("\n", 1)
    separated_numbers = parts[1]
    prefix = parts[0]
    separator = prefix[2]
    separated_numbers = normalize_separator(separated_numbers, separator)
    return separated_numbers


def normalize_separator(separated_numbers, separator):
    return separated_numbers.replace(separator, "\n")


def add_separated_numbers(separated_numbers, separator):
    numbers = separated_numbers.split(separator)
    result = 0
    for n in numbers:
        result += add(n)
    return result