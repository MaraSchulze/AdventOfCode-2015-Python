from get_input import get_input, get_test_input


def apply(wire, d):
    if wire.isdigit():
        return int(wire)
    if wire.isalpha() and type(d[wire]) != list:
        return apply(d[wire], d)

    operation = d[wire]
    if type(operation) == str:
        return int(operation)

    op = operation[-2]
    if op == "AND":
        result = apply(operation[0], d) & apply(operation[-1], d) % 2**16
    elif op == "OR":
        result = apply(operation[0], d) | apply(operation[-1], d) % 2**16
    elif op == "LSHIFT":
        result = apply(operation[0], d) << apply(operation[-1], d) % 2**16
    elif op == "RSHIFT":
        result = apply(operation[0], d) >> apply(operation[-1], d) % 2**16
    elif op == "NOT":
        result = ~apply(operation[-1], d) % 2**16
    else:
        print("Error")

    d[wire] = str(result)
    return result

# get input
inp = get_input(__file__)
d = {}
for line in inp:
    operation, wire = line.split(" -> ")
    left_side = operation.split()
    if len(left_side) == 1:
        d[wire] = left_side[0]
    else:
        d[wire] = left_side

# apply wires
result = apply("a", d)

# print result
print(result)
