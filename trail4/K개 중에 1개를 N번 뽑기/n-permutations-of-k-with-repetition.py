K, N = map(int, input().split())

arr = [0]*N

def choose(depth):
    if depth == N:
        print(*arr)
        return
    
    for i in range(1, K+1):
        arr[depth] = i
        choose(depth+1)
    
choose(0)


