n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

total = l+r+d

for _ in range(t):
    total.insert(0, total.pop())

l = total[:n]
r = total[n:len(total)-n]
d = total[len(total)-n:]

print(*l)
print(*r)
print(*d)