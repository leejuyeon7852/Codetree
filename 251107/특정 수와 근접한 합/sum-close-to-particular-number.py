import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))


min_value = sys.maxsize
total_sum = sum(arr)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        total = total_sum - (arr[i] + arr[j])
        min_value = min(min_value, abs(S-total))
        #print(f'total:{total}, min:{min_value}, {i}, {j+1}')

print(min_value)