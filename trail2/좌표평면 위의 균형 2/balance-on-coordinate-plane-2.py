n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

xs = sorted(set(p[0] for p in points))
ys = sorted(set(p[1] for p in points))

M = 0
ans = 999

for i in range(len(xs)):
    x = xs[i]+1
    for j in range(len(ys)):
        y = ys[j]+1
        count1 = 0 # 1사분면
        count2 = 0 # 2사분면
        count3 = 0 # 3사분먼
        count4 = 0 # 4사분면
        for px, py in points:
            if px < x and py > y:
                count1 += 1
            if px > x and py > y:
                count2 += 1
            if px < x and py < y:
                count3 += 1
            if px > x and py < y:
                count4 += 1
        M = max(count1, count2, count3, count4)
        ans = min(M, ans)

print(ans)