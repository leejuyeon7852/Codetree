arr = list(map(int, input().split()))
arr = sorted(arr)
S = arr[-1]

a = arr[0]
b = arr[1]

c = S - (a + b)

print(a, b, c)