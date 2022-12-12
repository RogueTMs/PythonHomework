def coroutine(func):
    def nxt(*args, **kwargs):
        n_func = func(*args, **kwargs)
        next(n_func)
        return n_func
    return nxt


@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


st = storage()
print(st.send(42))
print(st.send(42))
