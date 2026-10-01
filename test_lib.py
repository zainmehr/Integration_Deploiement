from lib import average, add


def test_average():
    assert average([11, -11, 10, 20]) == 7.5
    assert average([2, 4, 6]) == 4
    assert average([5]) == 5

print(add(2, 2))