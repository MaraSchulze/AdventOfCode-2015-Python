from get_input import get_input, get_test_input
from itertools import permutations

# get input
inp = get_input(__file__)

# build set for permutations
cities = [line.split()[0] for line in inp] + [line.split()[2] for line in inp]
cities = list(set(cities))

# get permutations
routes = list(permutations(cities))

# build dict for distances
distances = {}
for line in inp:
    items = line.split()
    distances[(items[0], items[2])] = int(items[4])
    distances[(items[2], items[0])] = int(items[4])

# compute result
min_length = float("inf")
for route in routes:
    current_length = sum([distances[(city1, city2)] for city1, city2 in zip(route, route[1:])])
    min_length = min(min_length, current_length)

# print result
print(min_length)
