N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]
P.sort()

max_count = 0

for i in range(N):
    total = 0
    count = 0
    for j in range(N):
        p = P[j]
        if i == j:
            p //= 2
        if total + p <= B:
            total += p
            count += 1
        else:
            break
    max_count = max(max_count, count)

print(max_count)

