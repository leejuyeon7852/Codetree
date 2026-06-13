n = int(input())
adjacent = list(map(int, input().split()))

for i in range(1, n+1):
    A = [0] * n
    A[0] = i
    used = {i}   
    
    for j in range(1, n):
        A[j] = adjacent[j-1] - A[j-1]
        
        if A[j] < 1 or A[j] > n or A[j] in used:
            break
        
        used.add(A[j])
    else:
        print(*A)
        break  
        
        

