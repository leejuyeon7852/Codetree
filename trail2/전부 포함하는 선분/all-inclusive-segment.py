n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

starts = sorted(s for s, e in segments)
ends = sorted(e for s, e in segments)

min1, min2 = starts[0], starts[1]
max1, max2 = ends[-1], ends[-2]

count_min = starts.count(min1)
count_max = ends.count(max1)

ans = float('inf')

for s, e in segments:
    if s == min1 and count_min == 1: # 유일한 최솟값을 빼면
        new_min = min2
    else:
        new_min = min1
    
    if e == max1 and count_max == 1: # 유일한 최댓값을 빼면
        new_max = max2
    else:
        new_max = max1
    ans = min(ans, new_max-new_min)

print(ans)
