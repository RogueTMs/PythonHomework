my_list = [42, 13, 7]


def chain(*iter):
    for i in iter:
        yield from i


print(list(chain([1, 2, 3], ['a', 'b'], my_list)))
