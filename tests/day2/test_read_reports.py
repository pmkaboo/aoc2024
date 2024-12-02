from day2.read_reports import read_reports

def test_read_reports():
    expected = [
        [1, 2, 3],
        [33, 111, 2222]
    ]
    actual = read_reports("tests/day2/test_reports.txt")
    assert actual == expected
