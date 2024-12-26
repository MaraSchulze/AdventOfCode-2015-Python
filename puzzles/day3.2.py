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
i1, j1, i2, j2 = 0, 0, 0, 0
for direction in directions[::2]:
    i1, j1 = tuple_add((i1, j1), dirs[direction])
    houses.add((i1, j1))
for direction in directions[1::2]:
    i2, j2 = tuple_add((i2, j2), dirs[direction])
    houses.add((i2, j2))

result = len(houses)

# print result
print(result)
