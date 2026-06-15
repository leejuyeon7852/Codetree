import sys
a, b, x, y = map(int, input().split())

min_diff = sys.maxsize
# a 에서 b로 바로 이동하는 경우
diff = abs(a-b)
min_diff = min(min_diff, diff)

# x에서 y로 순간이동
diff = abs(a-x) + abs(y-b)
min_diff = min(min_diff, diff)

# y에서 x로 순간이동
diff = abs(a-y)+abs(x-b)
min_diff = min(min_diff, diff)


print(min_diff)

