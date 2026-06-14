n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

left = x1.index(max(x1))
right = x2.index(min(x2))

for i in [left, right]:
    remainings = segments[:i] + segments[i+1:]
    rx1 = [r[0] for r in remainings]
    rx2 = [r[1] for r in remainings]
    if max(rx1) <= min(rx2):
        print('Yes')
        break
else:
    print('No')