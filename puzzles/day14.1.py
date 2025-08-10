from get_input import get_input, get_test_input


def parse(inp):
    reindeers = [(int(items[3]), int(items[6]), int(items[13])) for line in inp if (items := line.split())]
    return reindeers


def race(reindeers, distance):
    distances = []
    for reindeer in reindeers:
        velocity, time, rest = reindeer
        part = time * [velocity] + rest * [0]
        current_distance = [part[i % len(part)] for i in range(distance)]
        distances.append(current_distance)
    return distances


# get input
inp = get_input(__file__)

# parse reindeer data
reindeers = parse(inp)

# execute race
distances = race(reindeers, 2503)

# get maximum distance
result = max([sum(distance) for distance in distances])

# print result
print(result)
