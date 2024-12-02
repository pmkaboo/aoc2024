from day2.check_damped_safety import check_damped_safety

def test_check_damped_safety():
    scenarios = [
        ([1, 2, 4, 7, 9], True),
        ([9, 7, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], True),
        ([5, 4, 6, 3, 2], True),
        ([1, 2, 3, 3, 4], True),
        ([8, 6, 4, 4, 1], True),
        ([1, 1, 2, 3, 4], True),
        ([9, 9, 8, 7, 6], True),
        ([1, 2, 3, 4, 4], True),
        ([9, 8, 7, 6, 6], True),
        ([1, 2, 3, 4, 3], True),
        ([9, 8, 7, 6, 7], True),
        ([2, 3, 1, 4, 3], False),
        ([6, 5, 7, 4, 5], False),
        ([5, 6, 4, 3, 2], True)
    ]
    for report, expected in scenarios:
        actual = check_damped_safety(report)
        assert actual == expected

