x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

min_x = min(x1, x2, a1, a2)
max_x = max(x1, x2, a1, a2)
min_y = min(y1, y2, b1, b2)
mxa_y = max(y1, y2, b1, b2)

x = max_x - min_x
y = mxa_y - min_y

if x > y:
    area = x*x
else:
    area = y*y

print(area)