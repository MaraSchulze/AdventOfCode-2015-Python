from get_input import get_input, get_test_input


def string_value(s):
    length = 2
    for c in s:
        if c == "\\" or c == "\"":
            length += 1  
    return length


# get input
inp = get_input(__file__)

# get length
result = sum([string_value(s) for s in inp])

# print result
print(result)
