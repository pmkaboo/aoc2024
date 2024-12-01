def calculate_similarity(arr1, arr2):
    similarity = 0
    occurences = {}

    for x in arr2:
        if occurences.get(x):
            occurences[x] += 1
        else:
            occurences[x] = 1
    for x in arr1:
        similarity += (x * occurences.get(x, 0))

    return similarity
