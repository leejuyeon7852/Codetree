K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]

count = 0
for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            continue
        is_high = True
        for k in range(K):
            pos_a = arr[k].index(a)
            pos_b = arr[k].index(b)
            if pos_a < pos_b:
                is_high = False
                break
        if is_high:
            count+= 1

print(count)
        