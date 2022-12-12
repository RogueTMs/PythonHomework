my_list = [42, 13, 7]


def chain(*iter):
    ans = []
    for i in iter:
        ans.extend(i)

    return ans


print(list(chain([1, 2, 3], ['a', 'b'], my_list)))
