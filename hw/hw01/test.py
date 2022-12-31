def compose1(f, g):
    return lambda x : f(g(x))

def square(x):
    return x * x

def tripare(x):
    return x * 3



def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
