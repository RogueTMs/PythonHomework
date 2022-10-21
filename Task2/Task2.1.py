# D = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832, "Ovchinnikov": 97832}
D = {("Ivanov", "Kulikov"): 97832, "Petrov": 55521, "Kuznecov": 97832, "Ovchinnikov": 97832}
ans = dict()
ind = -1

for i in D.items():
    try:
        if i[1] in ans.keys():
            if i[1] == ind:
                ans[i[1]] = (ans[i[1]],)
                ind = -1
            if type(ans[i[1]]) == tuple:
                ans[i[1]] = (*ans[i[1]], i[0])
            else:
                ans[i[1]] = (ans[i[1]], i[0])
        else:
            ans[i[1]] = i[0]

        if type(i[0]) == tuple:
            ind = i[1]
            print(ind)
        # print(i[0], i[1], ans)
    except TypeError:
        print('Invalid Types of Arguments')
        raise TypeError('Incompatible types of arguments')

print(ans)
