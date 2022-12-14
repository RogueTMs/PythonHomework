def cycle(itr):
    while True:
        yield from itr


test = cycle([1, 2, 3])

for i in test:
    print(i)
