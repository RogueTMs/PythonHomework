s1 = list(map(str, input().split()))
s2 = list(map(str, input().split()))
ans = []
if len(s1) > len(s2): s1, s2 = s2, s1

for i in range(len(s1)):
    s = (s1[i], s2[i])
    ans.append(s)

print(ans)
