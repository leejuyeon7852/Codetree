import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
#print(points)
area = 0
ans = sys.maxsize

for i in range(n):
    min_x = sys.maxsize
    min_y = sys.maxsize
    max_x = -sys.maxsize
    max_y = -sys.maxsize
    for j in range(n):
        if i==j:
            continue
        x, y = points[j]
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    area = (max_x-min_x) * (max_y-min_y)
    ans = min(ans, area)

print(ans)
        

