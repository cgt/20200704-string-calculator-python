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

def add(separated_numbers):
    if separated_numbers == "":
        return 0
    if "," in separated_numbers:
        numbers = separated_numbers.split(",")
        result = 0
        for n in numbers:
            result += add(n)
        return result
    elif "\n" in separated_numbers:
        numbers = separated_numbers.split("\n")
        result = 0
        for n in numbers:
            result += add(n)
        return result

    return int(separated_numbers)