def is_square1(n):
    if n >= 0:
        a = n ** 0.5
        return a % 1 == 0
    else:
        return False

# -----------------------------------------------------


def is_square2(n):
    return n > -1 and n ** 0.5 % 1 == 0


print(is_square1(-1), is_square2(-1))
print(is_square1(0), is_square2(0))
print(is_square1(3), is_square2(3))
print(is_square1(4), is_square2(4))
print(is_square1(25), is_square2(25))
print(is_square1(26), is_square2(26))