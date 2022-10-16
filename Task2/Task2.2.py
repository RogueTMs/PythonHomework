from functools import partial


def specialize(func, *args, **kwargs):
    return partial(func, *args, **kwargs)


def sum(x, y):
    return x + y


plus_one = specialize(sum, y=1)
just_two = specialize(sum, 1, 1)
print(plus_one(10), just_two())
