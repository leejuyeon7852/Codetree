N = int(input())
heights = [int(input()) for _ in range(N)]
H = 17

answer = 10**9  

for L in range(0, 101):  
    cost = 0
    for h in heights:
        if h < L:
            cost += (L - h) ** 2
        elif h > L + H:
            cost += (h - (L + H)) ** 2
    
    answer = min(answer, cost)

print(answer)