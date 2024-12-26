from get_input import get_input, get_test_input


def has_two_pairs(s):
    d = {}
    for i in range(len(s) - 1):
        substr = s[i:i + 2]
        if substr in d and abs(d[substr] - i) >= 2:
            return True
        else:
            d[substr] = i
    return False


def is_three_group(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False


def is_nice(s):
    rule1 = has_two_pairs(s)
    rule2 = is_three_group(s)
    return rule1 and rule2


# get input
inp = get_input(__file__)

# decide which string is naughty or nice
result = 0
for s in inp:
    result += 1 if is_nice(s) else 0

# print result
print(result)
