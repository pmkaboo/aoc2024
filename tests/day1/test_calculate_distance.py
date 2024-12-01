import pytest

from day1.calculate_distance import calculate_distance

def test_incorrect_input():
    with pytest.raises(Exception):
        calculate_distance([1], [1,2])

def test_calculate_distance():
    scenarios = [
        ([1, 2, 3], [1, 2, 3], 0),
        ([4, 8, 6], [3, 2, 1], 12),
        ([1, 2],    [3, 4],    4),
        ([8, 5],    [1, 2],    10),
        ([1, 2],    [4, 1],    2),
        ([1],       [10],      9)
    ]
    for arr1, arr2, expected in scenarios:
        actual = calculate_distance(arr1, arr2)
        assert actual == expected
