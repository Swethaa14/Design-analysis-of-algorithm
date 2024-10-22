import itertools
from math import sqrt

def distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def tsp(cities):
    start_city = cities[0]
    other_cities = cities[1:]
    min_distance = float('inf')
    best_path = []
    
    for perm in itertools.permutations(other_cities):
        current_path = [start_city] + list(perm) + [start_city]
        current_distance = sum(distance(current_path[i], current_path[i + 1]) for i in range(len(current_path) - 1))
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = current_path
    
    return min_distance, best_path

test_cases = [
    [(1, 2), (4, 5), (7, 1), (3, 6)],
    [(2, 4), (8, 1), (1, 7), (6, 3), (5, 9)]
]

for i, cities in enumerate(test_cases, 1):
    shortest_distance, shortest_path = tsp(cities)
    print(f"Test Case {i}:")
    print(f"Shortest Distance: {shortest_distance}")
    print(f"Shortest Path: {shortest_path}")
    print()
