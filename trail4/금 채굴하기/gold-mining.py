n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def diamond_sum(grid, cx, cy, k, n):
    total = 0
    for r in range(n):
        for c in range(n):
            if abs(r-cx) + abs(c-cy) <= k:
                total += grid[r][c]
    return total

max_gold = 0
for k in range(n+1):
    cost = k**2 + (k+1)**2    # 비용
    for cx in range(n): # 중심 (0,0) -> (0, 1)...
        for cy in range(n):
            gold = diamond_sum(grid, cx, cy, k, n)
            if gold * m >= cost: 
                max_gold = max(max_gold, gold)

print(max_gold)

