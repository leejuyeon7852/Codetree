N = int(input())
records = []
for _ in range(N):
    p, pos = map(int, input().split())
    records.append((p, pos))

last_pos = {}
count = 0

for p, pos in records:
    if p in last_pos:
        if last_pos[p] != pos:
            count += 1
    last_pos[p] = pos

print(count)