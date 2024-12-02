def calculate_distance(arr1: list[int], arr2: list[int]) -> int:
    if len(arr1) != len(arr2):
        raise Exception("Arrays must be of same length")

    _arr1 = sorted(arr1)
    _arr2 = sorted(arr2)
    distance = 0

    while len(_arr1) > 0:
        x1 = _arr1.pop()
        x2 = _arr2.pop()
        distance += abs(x1 - x2)

    return distance
