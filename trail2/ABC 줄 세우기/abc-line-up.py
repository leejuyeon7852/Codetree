n = int(input())
arr = list(input().split())

nums = [n for n in range(26)]

arr_num = []
for i in range(len(arr)):
    arr_num.append(ord(arr[i])-ord('A'))

count = 0
for i in range(n):
    for j in range(n - 1 - i):
        if arr_num[j] > arr_num[j+1]:
            arr_num[j], arr_num[j+1] = arr_num[j+1], arr_num[j]
            count += 1

print(count)


