def digit_sum_v1(n):
    """this function is my code @layeboly
    """
    nToString = str(n)
    if len(nToString) == 1:
        return n
    if n < 0:
        return (-1) * int(nToString[1]) + digit_sum_v1(int(nToString[2:]))
    else:
        return int(nToString[0]) + digit_sum_v1(int(nToString[1:]))


def digit_sum_v2(n):
    assert int(n), 'Vous devez saisir un entier'
    if len(str(n)) == 1:
        return n
    return int(str(n)[0]) % 10 + digit_sum_v2(int(str(n)[1:]))


def digit_sum_v3(n):
    assert n >= 0 and int(n) == n, 'Vous devez saisir un entier positif'
    if n // 10 == 0:
        return n
    return n % 10 + digit_sum_v3((n // 10))


def power(x, n):
    assert n >= 0 and int(n) == n, 'n doit etre positive'
    if n == 0:
        return 1
    return x * power(x, n - 1)

def pgcd(a, b):
    assert a == int(a) and b == int(b), 'a and b must be integer'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    if a == 0:
        return b
    m = min(a, b)
    n = max(a, b)
    r = n % m
    if r == 0:
        return m

    return pgcd(m, r)

def decimal_to_binary(decimal):

    if decimal // 2 == 0:
        return str(decimal % 2)

    return str(decimal_to_binary((decimal // 2))) + str(decimal % 2)


print(decimal_to_binary(11))
n = 11.5
if int(n) == n:
    print(11)
