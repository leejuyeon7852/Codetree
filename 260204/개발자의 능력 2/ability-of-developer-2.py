import sys

ability = list(map(int, input().split()))

total = sum(ability)

min_diff = sys.maxsize

for i in range (6):
    for j in range(i+1, 6):
        for k in range(6):
            for l in range(k+1, 6):
                if k == i or k == j or l == i or l == j:
                    continue
                sum1 = ability[i]+ability[j]
                sum2 = ability[k]+ability[l]
                sum3 = total - sum1 - sum2

                teams = [sum1, sum2, sum3]
                diff = max(teams) - min(teams)

                min_diff = min(min_diff, diff)

print(min_diff)



