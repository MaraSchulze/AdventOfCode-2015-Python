from get_input import get_input, get_test_input


def read_number(json, i):
    number = 0

    dimension = 0
    while json[i + dimension].isdigit():
        number = 10 * number + int(json[i + dimension])
        dimension += 1

    if i > 0 and json[i - 1] == "-":
        number = - number

    return (number, dimension)


def evaluate(stack_part):
    return sum([item for item in stack_part if type(item) == int])


def count_except_red_objects(json):
    stack = []

    i = 0
    while i < len(json):
        char = json[i]
        if char in ["{", "["]:
            stack.append(char)
        elif char.isdigit():
            number, dimension = read_number(json, i)
            stack.append(number)
            i += dimension - 1
        elif i < len(json) - 3 and json[i:i + 3] == "red":
            stack.append("red")
        elif char == "}":
            opening_parenthesis_index = len(stack) - 1 - list(reversed(stack)).index("{")
            if not "red" in stack[opening_parenthesis_index:]:
                stack[opening_parenthesis_index] = evaluate(stack[opening_parenthesis_index:])
                stack = stack[:opening_parenthesis_index + 1]
            else:
                stack = stack[:opening_parenthesis_index]
        elif char == "]":
            opening_parenthesis_index = len(stack) - 1 - list(reversed(stack)).index("[")
            stack[opening_parenthesis_index] = evaluate(stack[opening_parenthesis_index:])
            stack = stack[:opening_parenthesis_index + 1]         
        i += 1
        
    return stack[0]


# get input
inp = get_input(__file__)
json = inp[0]

# delete red objects
result = count_except_red_objects(json)

# print result
print(result)
