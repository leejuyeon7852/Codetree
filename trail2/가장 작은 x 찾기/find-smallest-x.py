import math

n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

left, right = ranges[-1]

for a, b in reversed(ranges[:-1]):
    left, right = math.ceil(left/2), right//2
    left, right = max(left, a), min(right, b)

left, right = math.ceil(left/2), right//2

print(left)