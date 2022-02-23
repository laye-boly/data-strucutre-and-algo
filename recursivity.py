def factorielle(n):
    assert n >= 0 and int(n) == n, 'the number must be postitive'
    if n == 0:
        return 1
    return n * factorielle(n - 1)


def fibonnaci(n):
    assert n >= 0 and int(n) == n, 'the number must be postitive'
    if n in [0, 1]:
        return n
    return fibonnaci(n-1) + fibonnaci(n-1)

