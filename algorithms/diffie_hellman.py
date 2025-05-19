def power(base, exponent, mod):
    return pow(base, exponent, mod)

def diffie_hellman_demo():
    p = 23
    g = 5
    a = 6
    b = 15

    A = power(g, a, p)
    B = power(g, b, p)

    secret_A = power(B, a, p)
    secret_B = power(A, b, p)

    return {
        'p': p,
        'g': g,
        'a': a,
        'b': b,
        'A': A,
        'B': B,
        'secret_A': secret_A,
        'secret_B': secret_B
    }
