n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

total = u+d

for _ in range(t):
    total.insert(0, total.pop())

u = total[:n]
d = total[n:]

print(*u)
print(*d)