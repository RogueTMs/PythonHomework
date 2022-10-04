N = int(input())
ans = 0
wtc = 1

if N < 0:
    ans += 1
    N = -N - 1
    wtc = 0

while N != 0:
    if N % 2 == wtc: ans += 1
    N = N >> 1

print(ans)
