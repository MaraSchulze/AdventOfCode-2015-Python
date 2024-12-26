from get_input import get_input, get_test_input


# get input
inp = get_input(__file__)
packets = [[int(x) for x in line.split("x")] for line in inp]

# calculate wrapping paper
result = 0
for packet in packets:
    packet.sort()
    a, b, c = packet
    result += 2 * a + 2 * b + a * b * c

# print result
print(result)
