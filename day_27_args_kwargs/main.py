
# *args
def add(*args):
    return sum(args)


print(add(8, 3, 2, 5))


# **kwargs
def calculate(n, **kwargs):
    print(kwargs)

    # for key, val in kwargs.items():
    #     print(key)
    #     print(val)

    n += kwargs["add"]
    n *= kwargs.get("multiply")
    print(n)


calculate(2, add=3, multiply=5)


# Both
def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
