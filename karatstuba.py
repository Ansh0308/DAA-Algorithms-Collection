def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    n_2 = n // 2

    a = x // 10**n_2
    b = x % 10**n_2
    c = y // 10**n_2
    d = y % 10**n_2

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    return ((ac * 10**(2 * n_2)) + bd + ((10**n_2)*(ad_bc)))
x=1234
y=5678
print(karatsuba(x,y))
