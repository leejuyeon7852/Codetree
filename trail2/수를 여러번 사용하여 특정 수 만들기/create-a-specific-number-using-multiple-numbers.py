A, B, C = map(int, input().split())

max_val = 0

for i in range(C//A+1):
    for j in range(C//B+1):
        sum = A*i + B*j
        if sum <= C:
            max_val = max(max_val, sum)

print(max_val)