from get_input import get_input, get_test_input


def parse_line(line):
    line = line.split()
    lowerright = line[-1]
    lowerright = [int(x) for x in lowerright.split(",")]
    upperleft = line[-3]
    upperleft = [int(x) for x in upperleft.split(",")]
    
    command = line[-4]
    if command == "on":
        function = lambda x : x + 1
    elif command == "off":
        function = lambda x : x - 1 if x > 0 else 0
    else:
        function = lambda x : x + 2

    return (function, upperleft[0], upperleft[1], lowerright[0], lowerright[1])


def count_lights(lights):
    result = 0
    for i in range(len(lights)):
        result += sum(lights[i])
    return result


# get input
inp = get_input(__file__)

# switch lights
lights = [[0 for _ in range(1000)] for _ in range(1000)]
for line in inp:
    command, x1, y1, x2, y2 = parse_line(line)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            lights[i][j] = command(lights[i][j])


# count lights that are on
result = count_lights(lights)

# print result
print(result)
