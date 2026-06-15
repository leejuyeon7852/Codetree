n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

flow = 0
sum = 0
for i in range(n):
    flow += A[i] - B[i] 
    sum += abs(flow)

print(sum)