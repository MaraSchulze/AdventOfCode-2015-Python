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


def award_points(distances):
    accumulated_distances = [[sum(distance[:i + 1]) for i in range(len(distance))] for distance in distances]
    points_table = [[0 for _ in range(len(distance))] for distance in distances]
    for second in range(len(accumulated_distances[0])):
        maximum = max([distance[second] for distance in accumulated_distances]) 
        for i in range(len(distances)):
            points_table[i][second] = 1 if accumulated_distances[i][second] == maximum else 0
    return points_table


# get input
inp = get_input(__file__)

# parse reindeer data
reindeers = parse(inp)

# execute race
distances = race(reindeers, 2503)

# award points
points_table = award_points(distances)

# get maximum distance
result = max([sum(points) for points in points_table])

# print result
print(result)
