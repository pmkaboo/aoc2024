from day1.read_input import read_input

def test_read_input():
    expected = (
        [10000, 10001, 20001, 20000, 1, 11, 111, 1111],
        [10000, 20000, 10002, 10000, 1, 11, 111, 1111]
    )
    actual = read_input("tests/day1/test_input.txt")
    assert actual == expected
