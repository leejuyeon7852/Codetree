def is_happy(seq, m):
    if m == 1:
        return True
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            count += 1
            if count >= m:
                return True
        else:
            count = 1
    return False

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

total = 0


for i in range(n):
    if is_happy(grid[i], m):
        total += 1

for j in range(n):
    col = [grid[i][j] for i in range(n)]
    if is_happy(col, m):
        total += 1

print(total)