from get_input import get_input, get_test_input
import re


def string_value(s):
    length = 2
    i = 0
    while i < len(s):
        if s[i] == '\\':
            if s[i + 1] == '\\':
                length += 1
                i += 1
            if s[i + 1] == '"':
                length += 1
                i += 1
            if s[i + 1] == "x" and re.search(r"[\da-fA-F]{2}", s[i + 2:i + 4]):
                length += 3
                i += 3
        i += 1

    return length


# get input
inp = get_input(__file__)

# get length
result = sum([string_value(s) for s in inp])

# print result
print(result)
