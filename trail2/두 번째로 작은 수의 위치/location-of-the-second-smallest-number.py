n = int(input())
a = list(map(int, input().split()))

s = sorted(set(a))
if len(s) < 2:
    print(-1)
else:
    target = s[1]
    idx = -1
    cnt = 0
    for i in range(n):
        if a[i] == target:
            idx = i
            cnt += 1
    print(idx + 1 if cnt == 1 else -1)