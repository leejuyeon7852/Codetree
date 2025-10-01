N = int(input())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if i < j < k and A[i] <= A[j] <= A[k]:
                count+= 1
                #print(f'{i}, {j}, {k} | {A[i]}, {A[j]}, {A[k]} | {count}')
print(count)