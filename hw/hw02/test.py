def improve(update, close, guess = 1, max_times = 100):
    k = 0
    while not close(guess) and k < max_times:
        guess = update(guess)
        k += 1
    return guess

def appro_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def curried_pow(x):
    return lambda y : pow(x, y)

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start += 1
    
def curry2(f):
    return lambda x : lambda y : f(x, y)

def uncurry2(g):
    return lambda x, y : g(x)(y)


def find_zero(f, df):
    def close_zero(x):
        return appro_eq(f(x), 0)
    return improve(newton_update(f, df), close_zero)

def square_root(a):
    return find_zero(lambda x : x*x - a, lambda x : x*x)


def newton_update(f, df):
    return lambda x : x - f(x) / df(x)

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    for i in range(1, n + 1):
        if cond(i):
            print(i)
    


def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def fff(f):
        for i in range(1, n + 1):
            if f(i):
                print(i)
    return fff

def print_all(x):
    print(x)
    return print_all

def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n+k)
    return next_sum

def print_delayed(x):
    """Return a new function. This new function, when called,
    will print out x and return another function with the same
    behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    # >>> f("hi")
    # 5
    # # <function print_delayed> # a function is returned
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print


def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print