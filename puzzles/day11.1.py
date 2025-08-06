from get_input import get_input, get_test_input


def count_up(password, i):
    if i == -1:
        return password
    if password[i] != "z":
        password[i] = chr(ord(password[i]) + 1)
        return password

    password[i] = "a"
    return count_up(password, i - 1)


def create_next_password(password):
    password_as_list = list(password)
    password_as_list = count_up(password_as_list, len(password) - 1)
    return "".join(password_as_list)


def requirement1(password):
    return any([ord(c1) + 1 == ord(c2) and ord(c1) + 2 == ord(c3) for c1, c2, c3 in zip(password, password[1:], password[2:])])


def requirement2(password):
    nr_pairs = 0
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            nr_pairs += 1
            i += 1
        i += 1
    return nr_pairs >= 2


def requirement3(password):
    for i in range(len(password)):
        if password[i] in ["i", "o", "l"]:
            return False
    return True


# get input
inp = get_input(__file__)
password = inp[0]

# create new password
while not (requirement1(password) and requirement2(password) and requirement3(password)):
    password = create_next_password(password)

# print result
print(password)
