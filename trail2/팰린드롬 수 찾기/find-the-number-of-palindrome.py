X, Y = map(int, input().split())

count = 0

for n in range(X, Y+1):
    flag = True
    n = list(map(int, str(n)))
    for i in range(len(n)//2):
        if n[i] != n[len(n)-1-i]:
            flag = False
            break    
    if flag:
        count += 1

print(count)
                   