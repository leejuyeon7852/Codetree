N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_B = sorted(B)

count = 0
for i in range(N-M+1):
    sub_A = A[i: i+M]
    sorted_A = sorted(sub_A)

    if sorted_A == sorted_B:
        count += 1
print(count)

