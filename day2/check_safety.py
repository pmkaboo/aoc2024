def check_safety(report: list[int]) -> bool:
    prev = None
    direction = None

    for x in report:
        if prev:
            if direction is None:
                direction = prev > x
            if (prev > x) != direction:
                return False

            diff = abs(prev - x)
            if diff > 3 or diff < 1:
                return False
        prev = x

    return True
