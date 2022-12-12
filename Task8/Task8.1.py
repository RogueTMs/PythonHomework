from numpy import take
import itertools


def cycle(itr):
    cur = 0

    def step():
        nonlocal cur
        res = itr[cur]
        cur += 1
        if cur == len(itr):
            cur = 0
        return res

    return iter(step, None)


print(take(itertools.cycle([1, 2, 3]), 10))
