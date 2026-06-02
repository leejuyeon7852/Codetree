from collections import defaultdict

T, a, b = map(int, input().split())
c = []
x = []
d = defaultdict(list)
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))
    d[char].append(int(pos))
    

count = 0
for k in range(a, b+1):
    d1 = min(abs(k - pos) for pos in d["S"])
    d2 = min(abs(k-pos) for pos in d["N"])

    if d1 <= d2:
        count += 1

print(count)
