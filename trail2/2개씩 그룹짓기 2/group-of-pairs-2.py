n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

first = arr[:n]
second = arr[n:]

min_diff = float('inf')
for i in range(n):
    diff = second[i] - first[i]
    min_diff = min(min_diff, diff)

print(min_diff)