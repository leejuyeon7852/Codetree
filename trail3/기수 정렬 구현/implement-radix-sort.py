n = int(input())
arr = list(map(int, input().split()))

def radix_sort(arr, k):
    for pos in range(k):
        arr_new = [[] for _ in range(10)]
        for i in range(n):
            digit = (arr[i] // (10 ** pos)) % 10
            arr_new[digit].append(arr[i])
        
        store_arr = []
        for i in range(10):
            for j in range(len(arr_new[i])):
                store_arr.append(arr_new[i][j])
        arr = store_arr
    return arr

k = len(str(max(arr)))  
arr = radix_sort(arr, k)
print(*arr)