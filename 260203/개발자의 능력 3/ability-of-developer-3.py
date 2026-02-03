import sys
abilities = list(map(int, input().split()))
n = len(abilities)

def get_diff(i, j, k):
    sum1 = abilities[i]+abilities[j]+abilities[k]
    sum2 = sum(abilities)-sum1
    return abs(sum1-sum2)

min_diff = sys.maxsize
for i in range (n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            min_diff = min(min_diff, get_diff(i, j, k))

print(min_diff)
