n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort()

L_max = [0] * n # 왼쪽 큰거
R_min = [0] * n # 오른쪽 작은 

curr_max = -float('inf')
for i in range(n):
    L_max[i] = curr_max
    curr_max = max(curr_max, points[i][1])

curr_min = float('inf')
for i in range(n-1, -1, -1):
    R_min[i] = curr_min
    curr_min = min(curr_min, points[i][1])

ans = 0
for i in range(n):
    x1, x2 = points[i]
    # print(L_max[i], x2, R_min[i])
    if L_max[i] < x2 and x2 < R_min[i]:
        ans += 1
# print(points)
# print(L_max)
# print(R_min)
print(ans)