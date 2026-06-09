n, m = map(int, input().split())
pairs = []
for _ in range(m):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    pairs.append((a, b))

d = {}
for pair in pairs:
    d[pair] = d.get(pair, 0) + 1

print(max(d.values()))



