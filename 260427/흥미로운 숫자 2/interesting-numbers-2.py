from collections import Counter

X, Y = map(int, input().split())

ant = 0

def is_interesting(n):
    count = Counter(str(n))
    return len(count) == 2 and 1 in count.values()

for i in range(X, Y+1):
    if is_interesting(i) == True:
        ant += 1

print(ant)