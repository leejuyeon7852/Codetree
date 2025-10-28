a = input()
a = list(map(int, a))

flag = False
for i in range(1, len(a)):
    if a[i] == 0:
        a[i] = 1
        falg = True
        break
if flag == False:
    a[len(a)-1] = 0

N = 0
for i in range(len(a)-1, -1, -1):
    N += a[i]*2**(len(a)-1-i)
print(N)
    