from functools import partial


def specialize(func, *args, **kwargs):
    def ans(*arg, **kwarg):
        newkwargs = {**kwargs, **kwarg}
        return func(*args, *arg, **newkwargs)

    return ans


def sum(x, y):
    return x + y


plus_one = specialize(sum, y=1)
just_two = specialize(sum, 1, 1)
print(plus_one(10), just_two())
