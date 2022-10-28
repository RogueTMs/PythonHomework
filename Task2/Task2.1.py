# D = {("Ivanov", "Kulikov"): 97832, "Petrov": 55521, "Kuznecov": 97832, "Ovchinnikov": 97832}
D = {("Ivanov", "Kulikov"): 97832, "Petrov": 55521, ("abc", "a"): -1, "Kuznecov": 97832, "Ovchinnikov": 97832}
ans = dict()

for key, value in D.items():
    try:
        if value not in ans.keys():
            ans[value] = (key, )
        else:
            ans[value] += (key, )

    except TypeError:
        print('Invalid Types of Arguments')
        raise TypeError('Incompatible types of arguments')

for key, value in ans.items():
    if len(value) == 1:
        ans[key] = value[0]

print(ans)
