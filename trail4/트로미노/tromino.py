n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

shapes = [
    [(0, 0), (0, 1), (0, 2)], # 길쭉한 것 가로
    [(0, 0), (1, 0), (2, 0)], # 길쭉한 것 세로
    [(0, 0), (0, 1), (1, 0)], # L자 종류1
    [(0, 0), (1, 0), (1, 1)], # L자
    [(0, 0), (0, 1), (1, 1)], 
    [(0, 1), (1, 0), (1, 1)], 
]

max_total = 0
for i in range(n):
    for j in range(m):
        for shape in shapes:
            total = 0
            valid = True
            for dr, dc in shape:
                r, c = i+dr, j+dc
                if r >= n or c >= m:
                    valid = False
                    break
                total += grid[r][c]
            if valid:
                max_total = max(max_total, total)

print(max_total)
                