from math import gcd

def rational(n, d):
    """"""
    g = gcd(n, d)
    return [n//g, d//g]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def add_rational(x, y):
    nx, dx = numer(x), denom(x)


def f(x):
    def g(y):
        return x
    return g
    