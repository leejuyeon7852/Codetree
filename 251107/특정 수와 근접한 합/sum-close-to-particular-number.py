import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))



min_value = sys.maxsize
for i in range(N):
    for j in range(N-1):
        total = sum(arr)
        total -= (arr[i] + arr[j+1])
        min_value = min(min_value, abs(S-total))
        #print(f'total:{total}, min:{min_value}, {i}, {j+1}')

print(min_value)