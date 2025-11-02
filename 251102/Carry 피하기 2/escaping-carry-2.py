n = int(input())
arr = [int(input()) for _ in range(n)]

def is_carry(a, b, c):
    while a > 0 or b > 0 or c > 0:
        if a % 10 + b % 10 + c % 10 >= 10:
            return False
        a //= 10
        b //= 10
        c //= 10
    return True


max_sum = -1
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if is_carry(arr[i], arr[j], arr[k]):
                total = arr[i] + arr[j] + arr[k]
                # print(f'arr[i]:{arr[i]}, arr[j]:{arr[j]}, arr[k]:{arr[k]}')
                # print(f'total: {total}')
                max_sum = max(max_sum, total)            
print(max_sum)
