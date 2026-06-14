n, k = map(int, input().split())
arr = list(map(int, input().split()))

MAX_SIZE = 10000

min_cost = float('inf')

for a in range(1, MAX_SIZE+1):
    cost = 0
    for e in arr:
        if a <= e and e <= a + k:
            continue
        elif e < a:
            cost += a - e
        else:
            cost += e - (a+k)
    min_cost = min(min_cost, cost)

print(min_cost)