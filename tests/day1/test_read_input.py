from day1.read_input import read_input

def test_file_reading():
    expected = ([10000, 10001, 20000, 20001], [10000, 20000, 10002, 10000])
    actual = read_input("tests/day1/input.txt")
    assert actual == expected

if __name__ == "__main__":
    test_file_reading()
    print("all good")
