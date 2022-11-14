from functools import partial


def deprecated(f=None, *, since=None, will_be_removed=None):
    if f is None:
        return partial(deprecated, since=since, will_be_removed=will_be_removed)

    def inner(*args, **kwargs):
        s = f"Warning: function {f.__name__} is deprecated"
        if since:
            s += f" since version {since}."
        else:
            s += "."
        if will_be_removed:
            s += f" It will be removed in version {will_be_removed}"
        else:
            s += " It will be removed in future versions"

        print(s)

        return f(*args, **kwargs)

    return inner


@deprecated
def foo():
    print("Hello from foo")


@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar():
    print("Hello from bar")


bar()
foo()
