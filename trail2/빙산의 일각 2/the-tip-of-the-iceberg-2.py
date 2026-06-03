n = int(input())
h = [int(input()) for _ in range(n)]

max_count = 0

for i in range(0, max(h)):
    count = 0
    for k in range(n):
        if h[k] > i:
            if k == 0 or h[k-1] <= i:
                count += 1
    max_count = max(max_count, count)

print(max_count)       
        
