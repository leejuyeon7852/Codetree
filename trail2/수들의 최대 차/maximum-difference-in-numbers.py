N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()
max_length = 0

for i in range(N):
    lst = []
    for j in range(N):
        if 0 <= arr[j] - arr[i] <= K:
            lst.append(arr[j])
    max_length = max(max_length, len(lst))

print(max_length)