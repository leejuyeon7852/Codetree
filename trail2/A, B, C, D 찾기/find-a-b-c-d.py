arr = list(map(int, input().split()))

arr = sorted(arr)

s = arr[-1]
a = arr[0]
b = arr[1]

def get_sum(A, B, C, D):
    return [
        A, B, C, D, 
        A+B, B+C, C+D, D+A, A+C, B+D, 
        A+B+C, A+B+D, A+C+D, B+C+D, 
        A+B+C+D
        ]

for c in arr:
    if c >= b and c <= a + b:
        d = s - a - b - c
        if sorted(get_sum(a, b, c, d)) == arr:
            print(a, b, c, d)
            break