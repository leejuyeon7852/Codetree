A = input()
A = list(A)

count = 0
for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i] == '(' and A[j] == ')':
            count += 1
print(count)
