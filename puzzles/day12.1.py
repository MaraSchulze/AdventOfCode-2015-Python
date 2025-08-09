from get_input import get_input, get_test_input


def count_numbers(json):
    result = 0
    current_number, sign = 0, 1
    for i in range(len(json)):
        current_char = json[i]
        if current_char.isdigit():
            current_number = 10 * current_number + int(current_char)
        elif current_char == "-":
            sign = -1
        else:
            result += sign * current_number
            current_number = 0
            sign = 1
    return result


# get input
inp = get_input(__file__)
json = inp[0]

# count numbers
result = count_numbers(json)

# print result
print(result)
