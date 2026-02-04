N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def distance(a, b, N):
    diff = abs(a-b)
    return min(diff, N - diff) <= 2

def check(i, j, k):
    # 첫번째
    cond1 = distance(a1, i, N) and distance(b1, j, N) and distance(c1, k, N)
    # 두번째
    cond2 = distance(a2, i, N) and distance(b2, j, N) and distance(c2, k, N)
    # 둘 중 하나라고 T면 T 
    return cond1 or cond2

count = 0
for i in range (1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if check(i, j, k):
                count += 1

print(count)
            
