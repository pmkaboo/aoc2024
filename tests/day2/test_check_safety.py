from day2.check_safety import check_safety

def test_check_safety():
    scenarios = [
        ([1, 2, 4, 7, 9], True),
        ([9, 7, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([5, 4, 6, 3, 2], False),
        ([1, 2, 3, 3, 4], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 1, 2, 3, 4], False),
        ([9, 9, 8, 7, 6], False),
        ([1, 2, 3, 4, 4], False),
        ([9, 8, 7, 6, 6], False),
        ([1, 2, 3, 4, 3], False),
        ([9, 8, 7, 6, 7], False)

    ]
    for report, expected in scenarios:
        actual = check_safety(report)
        assert actual == expected

