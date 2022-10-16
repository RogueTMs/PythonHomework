D = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832, "Ovchinnikov": 97832}
ans = dict()

for i in D.items():
    try:
        if i[1] in ans.keys():
            if type(ans[i[1]]) == tuple:
                ans[i[1]] = (*ans[i[1]], i[0])
            else:
                ans[i[1]] = (ans[i[1]], i[0])
        else:
            ans[i[1]] = i[0]
        # print(i[0], i[1])
    except TypeError:
        print('Invalid Types of Arguments')
        raise TypeError('Incompatible types of arguments')

print(ans)
