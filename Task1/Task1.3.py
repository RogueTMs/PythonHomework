ans = []
s = input()
a = list(map(str, s.split("|")))
for x in a:
    ans.append(list(map(float, x.split())))

print(ans[0][1], ans)
