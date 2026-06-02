n = int(input())
a = list(map(int, input().split()))

ans = 0
for k in range(1, 101):
    count = 0
    for i in range(n):
        for j in range(i+1, n): 
            if a[i] + a[j] == 2 * k:
                count += 1
    ans = max(ans, count)


print(ans)