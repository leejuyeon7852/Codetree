n = int(input())
arr = list(map(int, input().split()))

def bubble_sort(arr):
    size = len(arr)

    for i in range(size-1):
        for j in range(size-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr

arr = bubble_sort(arr)

print(*arr)