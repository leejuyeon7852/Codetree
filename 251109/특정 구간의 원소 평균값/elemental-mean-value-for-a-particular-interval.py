n = int(input())
arr = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(i, n):
        total = 0
        for k in range(i, j+1):
            total += arr[k]
            #print(f'i:{i}, j:{j}, k:{k}')
        length = j - i + 1
        
        if total % length == 0:
            avg = total // length
            for k in range(i, j + 1):
                if avg == arr[k]:
                    count += 1
                    break

print(count)