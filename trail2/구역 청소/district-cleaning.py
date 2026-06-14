a, b = map(int, input().split())
c, d = map(int, input().split())

cnt = 0
if b < c or d < a: # 겹치지 않을 때
    cnt = (b-a) + (d-c)
else:
    cnt = max(a, b, c, d) - min(a, b, c, d)

print(cnt)
