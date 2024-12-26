from get_input import get_input, get_test_input


# get input
inp = get_input(__file__)
elevator = inp[0]

# compute floor
floor = 0
for i in range(len(elevator)):
    bracket = elevator[i]
    floor += 1 if bracket == "(" else -1
    if floor == -1:
        result = i + 1
        break

# print result
print(result)
