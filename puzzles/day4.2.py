import hashlib


# input
secret = "iwrupvqb"

# compute hash
integer = 0
hexstring = ""
while not hexstring.startswith("000000"):
    integer += 1
    secret_new = secret + str(integer)
    hash = hashlib.md5(secret_new.encode("utf-8"))
    hexstring = hash.hexdigest()

# print result
print(integer)
