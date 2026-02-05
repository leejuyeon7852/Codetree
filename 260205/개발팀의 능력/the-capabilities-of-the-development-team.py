import sys

arr = list(map(int, input().split()))
n=5

total = sum(arr)
sum1 = 0
sum2 = 0
sum3 = 0
min_diff = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        for k in range(n):
            for l in range(k+1, n):
                if k == i or k == j or l == i or l == j:
                    continue
                
                sum1 = arr[i]+arr[j]
                sum2 = arr[k]+arr[l]
                sum3 = total-sum1-sum2
                #print(f'sum1:{sum1}, sum2:{sum2}, sum3:{sum3}')

                if len({sum1, sum2, sum3}) != 3:
                    continue
                
                diff = max(sum1, sum2, sum3) - min(sum1, sum2, sum3)
                min_diff = min(min_diff, diff)

if min_diff == sys.maxsize:
    print("-1")
else:
    print(min_diff)         
