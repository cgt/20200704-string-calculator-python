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

def add(comma_separated_numbers):
    if comma_separated_numbers == "":
        return 0
    if "," in comma_separated_numbers:
        numbers = comma_separated_numbers.split(",")
        return add(numbers[0]) + add(numbers[1])

    return int(comma_separated_numbers)