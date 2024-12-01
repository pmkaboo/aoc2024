from .read_input import read_input
from .calculate_distance import calculate_distance
from .calculate_similarity import calculate_similarity

if __name__ == "__main__":
    input = read_input("day1/input.txt")
    distance = calculate_distance(*input)
    similarity = calculate_similarity(*input)
    print(f"distance: {distance}")
    print(f"similarity: {similarity}")
