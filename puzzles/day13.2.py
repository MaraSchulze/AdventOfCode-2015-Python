from get_input import get_input, get_test_input
from itertools import permutations


def build_happyness_table(inp):
    d = {}
    for line in inp:
        line = line[:-1].split()
        a, b, sign, points = line[0], line[10], line[2], line[3]
        d[(a, b)] = int(points) * (1 if sign == "gain" else -1)
        d[("I", a)] = 0
        d[(a, "I")] = 0
    return d


def create_permutations(inp):
    guests = {line.split()[0] for line in inp}
    guests.add("I")
    return permutations(guests)


def find_best_seating(permutations, happyness):
    maximum = 0
    for perm in permutations:
        seating = perm + (perm[0], )
        current_points = sum([happyness[(a, b)] + happyness[(b, a)] for a, b in zip(seating[:-1], seating[1:])])
        maximum = max(maximum, current_points)
    return maximum


# get input
inp = get_input(__file__)

# build happyness table
happyness = build_happyness_table(inp)

# create permutations
permutations = create_permutations(inp)

# find maximum score
result = find_best_seating(permutations, happyness)

# print result
print(result)
