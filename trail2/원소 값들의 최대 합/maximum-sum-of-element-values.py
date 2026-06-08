n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

max_sum = 0

for start in range(1, n+1):  
    sum = 0
    curr = start
    for _ in range(m):
        next = arr[curr]
        curr = next
        sum += next
    max_sum = max(max_sum, sum)
       
print(max_sum)
