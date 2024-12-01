def read_input(path: str) -> tuple[list[int], list[int]]:
    arr1 = []
    arr2 = []
    with open(path, "r") as file:
        for line in file.read().split("\n"):
            if line.strip(): # skip empty lines
                x1, x2 = line.split("   ")
                arr1.append(int(x1))
                arr2.append(int(x2))
    return arr1, arr2
