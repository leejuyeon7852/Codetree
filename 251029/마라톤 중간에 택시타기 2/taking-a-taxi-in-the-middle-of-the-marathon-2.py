import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_distance = sys.maxsize

# 거리 계산
def get_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

full_distance = 0
for i in range(n):
    if i + 1 < n:
        full_distance += get_distance(points[i], points[i+1])

# 건너뛴 거리 구하기
for i in range(1, n-1):
    removed = get_distance(points[i-1], points[i]) + get_distance(points[i], points[i+1])
    add = get_distance(points[i-1], points[i+1])
    result = full_distance - removed + add
    min_distance = min(min_distance, result)

print(min_distance)

    
        


    
