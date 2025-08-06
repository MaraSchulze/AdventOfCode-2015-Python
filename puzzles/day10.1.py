from get_input import get_input, get_test_input


def produce_sequence(sequence):
    current_number = sequence[0]
    length = 0
    next_sequence = ""
    for number in sequence:
        if number == current_number:
            length += 1
        else:
            next_sequence += str(length) + current_number
            current_number = number
            length = 1
    next_sequence += str(length) + current_number
    return next_sequence

# get input
inp = get_input(__file__)
sequence = inp[0]

# produce sequence
for _ in range(40):
    sequence = produce_sequence(sequence)
result = len(sequence)

# print result
print(result)
