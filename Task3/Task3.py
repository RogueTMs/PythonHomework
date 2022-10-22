def flatten(arr, depth=-1):
    ans = []
    for i in arr:
        if type(i) != list:
            ans.append(i)
        else:
            if depth != 0:
                ans += flatten(i, depth - 1)
            else:
                ans.append(i)
    return ans


print(flatten([1, 2, [4, 5], [6, [7]], 8]))
