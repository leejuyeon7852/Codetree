n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

r = max(x)
arr=['']*(r+1)
for i in range(n):
    arr[x[i]] = c[i]  # pos 위치에 char 저장

max_value = 0
for i in range(1, r-k+1):
    total = 0
    for j in range(i, i+k+1):
        if arr[j] == 'G':
            total += 1
            #print(f'{j}:{arr[j]}, {total}')
        elif arr[j] == 'H':
            total += 2
            #print(f'{j}:{arr[j]}, {total}')
        #print(f'{j}:{arr[j]}, {total}')
    max_value = max(max_value, total)
print(max_value)   

