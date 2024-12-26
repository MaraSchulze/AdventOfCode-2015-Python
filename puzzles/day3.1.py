from get_input import get_input, get_test_input


def tuple_add(a, b):
    a1, a2 = a
    b1, b2 = b 
    return (a1 + b1, a2 + b2)


# get input
inp = get_input(__file__)
directions = inp[0]

# deliver presents
dirs = {"^" : (-1, 0), "v" : (1, 0), "<" : (0, -1), ">" : (0, 1)}

houses = {(0, 0)}
i, j = 0, 0
for direction in directions:
    i, j = tuple_add((i, j), dirs[direction])
    houses.add((i, j))

result = len(houses)

# print result
print(result)
