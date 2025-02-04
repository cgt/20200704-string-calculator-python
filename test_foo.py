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
    with pytest.raises(Exception) as ex:
        add("-2")
    assert "error: negatives not allowed: -2" in str(ex.value)
    with pytest.raises(Exception) as ex:
        add("6,-7")
    assert "error: negatives not allowed: -7" in str(ex.value)
    with pytest.raises(Exception) as ex:
        add("1,-2,-3")
    assert "error: negatives not allowed: -2 -3" in str(ex.value)


def add(separated_numbers):
    if separated_numbers == "":
        return 0

    separated_numbers = normalize(separated_numbers)
    numbers = split_numbers(separated_numbers)

    validate_input(numbers)
    return sum(numbers)


def split_numbers(separated_numbers):
    numbers = separated_numbers.split("\n")
    numbers = [int(x) for x in numbers]
    return numbers


def normalize(separated_numbers):
    if has_custom_separator(separated_numbers):
        separated_numbers = normalize_custom_separator(separated_numbers)
    separated_numbers = normalize_separator(separated_numbers, ",")
    return separated_numbers


def has_custom_separator(separated_numbers):
    return separated_numbers.startswith("//")


def validate_input(numbers):
    raise_if_contains_negative_numbers(numbers)


def raise_if_contains_negative_numbers(numbers):
    invalid_inputs = [str(x) for x in numbers if x < 0]
    if len(invalid_inputs) > 0:
        raise Exception("error: negatives not allowed: {}".format(" ".join(invalid_inputs)))


def normalize_custom_separator(separated_numbers):
    parts = separated_numbers.split("\n", 1)
    separated_numbers = parts[1]
    prefix = parts[0]
    separator = prefix[2]
    separated_numbers = normalize_separator(separated_numbers, separator)
    return separated_numbers


def normalize_separator(separated_numbers, separator):
    return separated_numbers.replace(separator, "\n")


