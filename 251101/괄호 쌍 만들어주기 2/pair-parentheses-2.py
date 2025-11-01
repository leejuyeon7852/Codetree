A = input()
A = list(A)

count = 0
for i in range(len(A)):
    if i + 1 < len(A):
        if A[i] == '(' and A[i] == A[i+1]:
            for j in range(i+2, len(A)):
                if j + 1 < len(A):
                    if A[j] == ')' and A[j] == A[j+1]:
                        count += 1

print(count)