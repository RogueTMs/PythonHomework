from functools import partial


def deprecated(f=None, *, since="", will_be_removed=""):
    if f is None:
        return partial(deprecated, since=since, will_be_removed=will_be_removed)

    def inner(*args, **kwargs):
        l_since, l_will_be_removed = len(since), len(will_be_removed)
        if l_since != 0 and l_will_be_removed != 0:
            print(f"Warning: function {f.__name__} is deprecated since version {since}."
                  f" It will be removed in version {will_be_removed}")
        elif l_since == 0 and l_will_be_removed != 0:
            print(f"Warning: function {f.__name__} is deprecated. It will be removed in version {will_be_removed}")
        elif l_will_be_removed == 0 and l_since != 0:
            print(f"Warning: function {f.__name__} is deprecated since version {since}. "
                  f"It will be removed in future versions")
        else:
            print(f"Warning: function {f.__name__} is deprecated. It will be removed in future versions.")

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
