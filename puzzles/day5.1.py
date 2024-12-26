from get_input import get_input, get_test_input


def is_nice(s):
    rule1 = len([c for c in s if c in "aeiou"]) >= 3
    rule2 = any([s[:-1][i] == s[1:][i] for i in range(len(s) - 1)])
    rule3 = all([s[:-1][i:i+2] not in ["ab", "cd", "pq", "xy"] for i in range(len(s) - 1)])
    return rule1 and rule2 and rule3


# get input
inp = get_input(__file__)

# decide which string is naughty or nice
result = 0
for s in inp:
    result += 1 if is_nice(s) else 0

# print result
print(result)
