n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

for e in arr:
    if e % 2 != 0 and e % 3 == 0:
        print(e)