n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

max_t = 0

for i in range(n):
    worked_time = [0]*1001
    for j in range(n):
        if i == j:
            continue
            
        start, end = times[j]
        for t in range(start, end):
            worked_time[t] = 1
        
    time = sum(worked_time)
    max_t = max(max_t, time)

print(max_t)
