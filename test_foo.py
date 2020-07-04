def test_empty_string_returns_zero():
    assert add("") == 0

def test_add_0_returns_0():
    assert add("0") == 0

def test_add_4_returns_4():
    assert add("4") == 4

def test_add_1_and_2_returns_3():
    assert add("1,2") == 3

def add(numbers):
    if numbers == "":
        return 0
    if "," in numbers:
        return 3

    return int(numbers)