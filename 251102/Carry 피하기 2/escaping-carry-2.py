import sys
n = int(input())
arr = [int(input()) for _ in range(n)]


max_sum = -sys.maxsize
total = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            carry = False
            if (arr[i] % 100 // 10 + arr[j] % 100 // 10 + arr[k] % 100 // 10 >= 10):
                carry = True
            elif (arr[i] % 10 + arr[j] % 10 + arr[k] % 10 >= 10):
                carry = True
            if not carry:
                total = arr[i] + arr[j] + arr[k]
                #print(f'arr[i]:{arr[i]}, arr[j]:{arr[j]}, arr[k]:{arr[k]}')
                #print(f'total: {total}')
            max_sum = max(max_sum, total)

print(max_sum)
