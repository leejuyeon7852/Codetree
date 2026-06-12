nums = list(map(int, input().split()))

def get_sum(A, B, C, D):
    return [
        A, B, C, D, 
        A+B, B+C, C+D, D+A, A+C, B+D, 
        A+B+C, A+B+D, A+C+D, B+C+D, 
        A+B+C+D
        ]

A = sorted(nums)[0]
B = sorted(nums)[1]
S = max(nums)

for C in range(B, S):
    D = S - A - B - C
    if C <= D:
        if sorted(get_sum(A, B, C, D)) == sorted(nums):
            print(A, B, C, D)
            break