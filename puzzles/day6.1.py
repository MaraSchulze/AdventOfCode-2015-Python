from get_input import get_input, get_test_input


def parse_line(line):
    line = line.split()

    lowerright = line[-1]
    lowerright = [int(x) for x in lowerright.split(",")]

    upperleft = line[-3]
    upperleft = [int(x) for x in upperleft.split(",")]
    
    command = line[-4]
    if command == "on":
        function = lambda _ : True
    elif command == "off":
        function = lambda _ : False
    else:
        function = lambda x : not x

    return (function, upperleft[0], upperleft[1], lowerright[0], lowerright[1])


def switch_lights(line, lights):
    command, x1, y1, x2, y2 = parse_line(line)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            lights[i][j] = command(lights[i][j])


def count_lights(lights):
    result = 0
    for i in range(len(lights)):
        for j in range(len(lights[0])):
            result += 1 if lights[i][j] is True else 0
    return result


# get input
inp = get_input(__file__)

# create light panel
lights = [[False for _ in range(1000)] for _ in range(1000)]

# switch lights
for line in inp:
    switch_lights(line, lights)

# count lights that are on
result = count_lights(lights)

# print result
print(result)
