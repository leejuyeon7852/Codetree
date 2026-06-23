n = int(input())
arr = list(map(int, input().split()))

def selection_sort(arr):
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    return arr
    
arr = selection_sort(arr)
print(*arr)
