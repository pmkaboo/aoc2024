def calculate_similarity(arr1: list[int], arr2: list[int]) -> int:
    similarity = 0
    occurences: dict[int, int] = {}

    for x in arr2:
        if occurences.get(x):
            occurences[x] += 1
        else:
            occurences[x] = 1
    for x in arr1:
        similarity += (x * occurences.get(x, 0))

    return similarity
