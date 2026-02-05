import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_dist = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]

        dx = x1-x2
        dy = y1-y2
        dist = dx*dx + dy*dy
        min_dist = min(min_dist, dist)

print(min_dist)

        
        


            