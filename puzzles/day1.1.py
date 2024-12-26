from get_input import get_input, get_test_input


# get input
inp = get_input(__file__)
elevator = inp[0]

# compute floor
result = 0
for bracket in elevator:
    result += 1 if bracket == "(" else -1

# print result
print(result)
