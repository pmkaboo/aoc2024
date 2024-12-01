from day1.calculate_similarity import calculate_similarity

def test_calculate_similarity():
    scenarios = [
        ([1, 2], [1, 2], 3),
        ([1, 2], [2, 1], 3),
        ([1, 2], [1, 3], 1),
        ([1, 2], [3, 4], 0)
    ]
    for arr1, arr2, expected in scenarios:
        actual = calculate_similarity(arr1, arr2)
        assert actual == expected
